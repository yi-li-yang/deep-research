#!/usr/bin/env python3
"""Print a video's transcript as plain text, so Claude can read what was said.

    python3 transcript.py <video-url> [--lang ja] [--timestamps]

Uses the video's own captions (human-made first, then automatic) through yt-dlp,
which supports YouTube, Bilibili, Vimeo and many other sites. Nothing is downloaded
except the caption file.

Exit codes: 0 ok · 1 failed (e.g. no captions) · 3 yt-dlp missing · 4 blocked by the site.
"""
import argparse
import json
import re
import sys

BLOCKED_HINTS = ("confirm you're not a bot", "confirm you’re not a bot", "http error 429", "too many requests")
FORMAT_PREFERENCE = ("json3", "vtt", "srt")


def parse_json3(data):
    """YouTube json3 captions -> [(start_seconds, text)]."""
    cues = []
    for event in data.get("events", []):
        text = "".join(seg.get("utf8", "") for seg in event.get("segs") or []).strip()
        if text:
            cues.append((event.get("tStartMs", 0) / 1000, " ".join(text.split())))
    return cues


def parse_vtt(text):
    """WebVTT or SRT captions -> [(start_seconds, text)], with rolling-caption repeats removed."""
    cues, start, last = [], 0.0, None
    stamp = re.compile(r"(?:(\d+):)?(\d{2}):(\d{2})[.,](\d{3})\s+-->")
    for raw in text.splitlines():
        line = raw.strip()
        m = stamp.match(line)
        if m:
            h, mnt, s, ms = (int(g or 0) for g in m.groups())
            start = h * 3600 + mnt * 60 + s + ms / 1000
            continue
        if not line or line.isdigit() or line.startswith(("WEBVTT", "Kind:", "Language:", "NOTE")):
            continue
        line = " ".join(re.sub(r"<[^>]+>", "", line).split())  # drop inline timing/style tags
        if line and line != last:
            cues.append((start, line))
            last = line
    return cues


def render(cues, timestamps=False, window=60):
    """Group cues into paragraphs of about `window` seconds."""
    paragraphs, current, block_start = [], [], None
    for start, text in cues:
        if block_start is None:
            block_start = start
        if start - block_start >= window and current:
            paragraphs.append((block_start, " ".join(current)))
            current, block_start = [], start
        current.append(text)
    if current:
        paragraphs.append((block_start, " ".join(current)))
    out = []
    for start, text in paragraphs:
        prefix = f"[{int(start // 60):02d}:{int(start % 60):02d}] " if timestamps else ""
        out.append(prefix + text)
    return "\n\n".join(out)


def pick_track(info, lang=None):
    """Choose (kind, language, formats): human captions before automatic ones, original language first."""
    manual, auto = info.get("subtitles") or {}, info.get("automatic_captions") or {}
    native = info.get("language")
    if lang:
        wanted = [lang]
    else:
        wanted = [native, f"{native}-orig", "en", "en-orig"] if native else ["en", "en-orig"]
    for kind, tracks in (("human", manual), ("automatic", auto)):
        for code in wanted + [c for c in tracks if c.endswith("-orig")]:
            if code in tracks:
                return kind, code, tracks[code]
    if manual and not lang:  # human captions in another language still beat nothing
        code = next(iter(manual))
        return "human", code, manual[code]
    return None


def fail(message, code):
    print(message, file=sys.stderr)
    sys.exit(code)


def main():
    parser = argparse.ArgumentParser(description="Print a video's transcript as plain text.")
    parser.add_argument("url")
    parser.add_argument("--lang", help="caption language code, e.g. en, ja, zh-Hans (default: the video's own language)")
    parser.add_argument("--timestamps", action="store_true", help="prefix each paragraph with [mm:ss]")
    args = parser.parse_args()

    try:
        import yt_dlp
    except ImportError:
        fail("transcript.py needs yt-dlp. Install it with: python3 -m pip install --user yt-dlp", 3)

    class Silent:  # our own one-line messages replace yt-dlp's log output
        def debug(self, msg): pass
        def warning(self, msg): pass
        def error(self, msg): pass

    options = {"skip_download": True, "quiet": True, "no_warnings": True, "noplaylist": True, "logger": Silent()}
    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(args.url, download=False)
            track = pick_track(info, args.lang)
            if not track:
                fail("failed: this video has no captions" + (f" in '{args.lang}'" if args.lang else "")
                     + ". Record it as a pointer (who, timestamp, what) instead.", 1)
            kind, code, formats = track
            fmt = next((f for pref in FORMAT_PREFERENCE for f in formats if f.get("ext") == pref), None)
            if not fmt:
                fail(f"failed: no readable caption format for '{code}'.", 1)
            body = ydl.urlopen(fmt["url"]).read().decode("utf-8", "replace")
    except yt_dlp.utils.DownloadError as error:
        message = str(error).lower()
        if any(hint in message for hint in BLOCKED_HINTS):
            fail("blocked: the site refused requests from this network (common on cloud servers). "
                 "Run it from a home connection, or record the video as a pointer instead.", 4)
        fail("failed: " + str(error).splitlines()[0], 1)
    except Exception as error:  # extractor bugs and site changes surface as arbitrary exceptions
        fail(f"failed: yt-dlp could not read this site ({type(error).__name__}: {error}). "
             "Record the video as a pointer instead.", 1)

    cues =parse_json3(json.loads(body)) if fmt.get("ext") == "json3" else parse_vtt(body)
    date = info.get("upload_date") or ""
    if len(date) == 8:
        date = f"{date[:4]}-{date[4:6]}-{date[6:]}"
    print(f"# {info.get('title', '')}")
    print(f"{info.get('channel') or info.get('uploader', '')} · {date} · {info.get('webpage_url', args.url)}")
    print(f"Captions: {kind}, language '{code}'\n")
    print(render(cues, args.timestamps))


if __name__ == "__main__":
    main()

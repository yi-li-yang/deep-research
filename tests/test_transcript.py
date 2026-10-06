import importlib.util
import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "tests" / "fixtures"
spec = importlib.util.spec_from_file_location("transcript", ROOT / "skills/expertise/scripts/transcript.py")
transcript = importlib.util.module_from_spec(spec)
spec.loader.exec_module(transcript)


class ParseTests(unittest.TestCase):
    def test_vtt_drops_tags_and_rolling_repeats(self):
        cues = transcript.parse_vtt((FIXTURES / "youtube_auto.vtt").read_text())
        self.assertEqual([text for _, text in cues], [
            "hello everyone welcome",
            "to the patch review",
            "first the jungle changes",
        ])
        self.assertEqual(cues[-1][0], 65.11)

    def test_srt_is_parsed_like_vtt(self):
        cues = transcript.parse_vtt((FIXTURES / "plain.srt").read_text())
        self.assertEqual(cues, [(1.0, "Sharpen the blade first."),
                                (3.5, "Then set the chipbreaker close to the edge.")])

    def test_json3_skips_empty_events_and_normalises_spaces(self):
        cues = transcript.parse_json3(json.loads((FIXTURES / "youtube.json3").read_text()))
        self.assertEqual(cues, [(0.0, "hello everyone"), (2.1, "welcome to the review")])


class RenderTests(unittest.TestCase):
    def test_paragraphs_split_by_window_with_timestamps(self):
        cues = [(0, "a"), (30, "b"), (61, "c")]
        self.assertEqual(transcript.render(cues, timestamps=True), "[00:00] a b\n\n[01:01] c")
        self.assertEqual(transcript.render(cues), "a b\n\nc")


class TrackTests(unittest.TestCase):
    def test_human_captions_in_native_language_win(self):
        info = {"language": "ja", "subtitles": {"ja": ["h-ja"]},
                "automatic_captions": {"ja-orig": ["a-ja"], "en": ["a-en"]}}
        self.assertEqual(transcript.pick_track(info), ("human", "ja", ["h-ja"]))

    def test_automatic_original_language_beats_translation(self):
        info = {"language": "ja", "subtitles": {}, "automatic_captions": {"en": ["a-en"], "ja-orig": ["a-ja"]}}
        self.assertEqual(transcript.pick_track(info), ("automatic", "ja-orig", ["a-ja"]))

    def test_requested_language_and_no_captions(self):
        info = {"language": "en", "subtitles": {"en": ["h-en"]}, "automatic_captions": {}}
        self.assertIsNone(transcript.pick_track(info, lang="de"))
        self.assertIsNone(transcript.pick_track({"subtitles": {}, "automatic_captions": {}}))


if __name__ == "__main__":
    unittest.main()

# Agent 1 report: platform pages and feeds (checked 2026-10-07)

**Report file not written.** The Write tool refused `report-1.md` ("Subagents should return findings as text, not write report files"). My instructions say the same, so I did not retry by another route. The full table is in the appendix below and can be pasted into `report-1.md`. While retrying a search I wrote one temp JSON to `/tmp/claude-0/us_scx.json`. I deleted it and confirmed it is gone. I created no other file.

**Method.** Raw `curl` worked for everything: the iTunes lookup and search API returned raw JSON, and 小宇宙 pages expose `__NEXT_DATA__`. I also read the Ximalaya, Buzzsprout, xyzfm and Lizhi feeds, the NetEase public API, App Store pages and lookups, Spotify, the YouTube playlist Atom feed, the Hugging Face API and README, the Podwise post, and the RSSHub route source. I listened to no audio. I only tested that the audio enclosures can be fetched. No page addressed me or told me what to conclude.

## Counts per verdict (70 rows)
Rows merge atoms only when they share one source line and one verdict.

| Verdict | Rows |
|---|---|
| STATED | 54 |
| SCOPE | 14 |
| WRONG | 1 |
| NOT IN SOURCE | 1 |
| SUPERSEDED | 0 |

## Every non-STATED row, with a one-line fix
- **#38 WRONG, 我爱龙门阵 "main run 2018–2019".** The feed holds 225 episodes dated 2013-08-13 to 2019-05-23, plus one on 2023-08-21. Per year: 2013:30, 2014:39, 2015:41, 2017:56, 2018:50, 2019:8, 2023:1, so only 58 fall in 2018–2019. Fix: "225 episodes, 2013-08 to 2019-05, mostly 2013–2018, plus an anniversary episode on 2023-08-21".
- **#65 NOT IN SOURCE, RSSHub "may be rate-limited".** Neither the Podwise post nor the route source mentions rate limits. Fix: drop it, or mark it as the author's own caution.
- **#6 SCOPE, 野地电波 "55–100 minutes".** In the last 365 days (38 episodes) the median is 67 min and the range 54–162; 31 of 38 fall in 55–100. Fix: "typically 55–100 min (a few run to 160)".
- **#8 SCOPE, Apple 成都话 search "descriptions mention Chengdu … in Putonghua".** Of the 29 result pages whose descriptions I read, only 4 mention 成都. Most hits match 话 in titles (肥话连篇, 松果白话, 山下夜话, 一画一话, 仲有话说) or episode text. No description says the show is in Putonghua. The other 3 results are dialect shows. Fix: "32 shows, mostly irrelevant matches on 话 or episode text; only 3 are dialect shows, all dead".
- **#12 SCOPE, 喜马拉雅FM "(registration by phone number)".** The listing text does not say so. Its privacy label shows "Contact Info: Phone Number", and a 2019 user review says "I registered and logged in with my phone number". Fix: drop the parenthetical, or say a user review reports phone registration.
- **#18 SCOPE, 摆一哈 latest "about June 2026".** The latest episode (EP13) is 2026-05-29. Fix: "latest 2026-05-29".
- **#23 SCOPE, 山城龙门阵 "6–22 min".** Durations run 2.1–22.2 min, and six episodes are under 6 min. Fix: "2–22 min".
- **#27 SCOPE, 好生说Radio "mostly April 2021 to December 2022".** The first feed item is 2021-05-05 (2021:38 episodes, 2022:17, last of the run 2022-12-04). Fix: "May 2021 to December 2022".
- **#32 SCOPE, 打脑壳 "25–135 min".** Episode 10 is 7.3 min and episode 02 about 23 min; the maximum is 135.3. Fix: "7–135 min".
- **#40 SCOPE, 轻松一刻四川话版 "13–18 min".** The range is 10.4–32.4 min with a median of 15.2; 427 of 489 fall in 13–18. Fix: "mostly 13–18 min (range 10–32)".
- **#41 SCOPE, 轻松一刻四川话版 "from 2015-09 (earliest seen, Vol. 64)".** Vol. 1 "鸡血人生" is dated 2015-04-24, and Vol. 64 is 2015-09-10. Fix: "from 2015-04-24 (Vol. 1) to 2018-10-16 (Vol. 489)".
- **#44 SCOPE, 德耒DELAY "about 2022".** The 小宇宙 page's latest episode is 2023-01-14, and all 11 episodes are dated 2023-01-08 to 2023-01-14. Fix: "last episode 2023-01-14".
- **#53 SCOPE, 府河小茶铺 "19,941 subscribers".** The live counter read 19,951 twice at check time. Fix: update it, or write "about 20,000".
- **#57 SCOPE, Hugging Face "licence is unverified".** The card's front matter declares `license: cc-by-4.0`. The repo holds only a README, and the data are downloaded from magichub.com. Fix: "card declares CC BY 4.0 (uploader-declared); data hosted at magichub.com".
- **#66 SCOPE, Himalaya "is the international edition of Ximalaya".** The listing says "a brainchild of Ximalaya 喜马拉雅". Fix: "a Ximalaya spin-off", or cite another source for "international edition".
- **#67 SCOPE, Himalaya "holds audiobooks and English courses".** The listing says "short audio courses and motivational stories". The what's-new text adds screen-adaptation audio dramas, BL audio dramas and children's stories. "Audiobooks" appears only in the app title, and "English" is never stated. Fix: "audio courses, stories and audio dramas; no Sichuanese content mentioned".

## Not checkable, or not mine
- **Judgement:** "most learner-friendly" (山城龙门阵). Support: its oldest episode's notes say "听不懂方言的朋友，阔以在弹幕网找到字幕版哟~" (a subtitled version exists on Bilibili).
- **Search-engine output:** "a search summary calling it mainly dialect" (摆一哈) and "a search snippet called it dialect stand-up" (洋芋摆巴适) cannot be reproduced. The show-page and feed halves are checked (#20, #52).
- **Coverage claim:** "only one show … describes itself as Sichuanese and is active" cannot be proved by a source, and nothing I opened contradicts it. The other active shows (摆一哈, 海椒Radio, 府河小茶铺) state no dialect, and no active self-described Sichuanese show appears among the Apple 成都话 hits.
- **Agent 2's group:** the 小宇宙 episode pages (100种生活, 废物没有假期, BreadToast) and the iOS app id1490232242 are assigned to Agent 2, and I did not open them. I reached every claim in my group.

## Notes for the caller
- **Date convention is mixed.** Feeds and Apple give GMT stamps. The briefing uses GMT dates for 野地电波 (09-22), 好生说Radio (05-12) and 龙门阵罪话 (05-10), but a China-time date for 山城龙门阵 (12-31, which is 2023-12-30 22:00 GMT). In China time the first three are 09-23, 05-13 and 05-11. Pick one convention.
- **Extra leads:**
  - 海椒Radio Vol.078 is an episode about 成都话 ("听一哈成都话是不是真的有点具体？！").
  - 轻松一刻四川话版 labels some episodes by variety (Vol. 63 南充话版, Vol. 64 成都话版).
  - 德耒DELAY's description is "四川话聊天节目".
  - Apple lists 海椒Radio twice (ids 1611031470 and 1652808757); Vol. 091 matches the second.
  - 摆一哈 EP13 notes say the hosts now live "分别生活在湾区与纽约".

---

## Appendix: full table (for `report-1.md`)

Legend (feeds):
- YD = http://www.ximalaya.com/album/33132000.xml
- SC = http://www.ximalaya.com/album/44160859.xml
- HS = https://www.ximalaya.com/album/47203982.xml
- WA = http://www.ximalaya.com/album/204097.xml
- YY = http://www.ximalaya.com/album/11136143.xml
- FY = https://www.ximalaya.com/album/78481728.xml
- DNK = https://rss.buzzsprout.com/2243225.rss
- LMZ = https://feed.xyzfm.space/el7u3lpqfq7l
- HJ = https://feed.xyzfm.space/mwtfernt99uy
- LZ = http://rss.lizhi.fm/rss/612841.xml

Legend (other sources):
- A-id = https://podcasts.apple.com/cn/podcast/id<id>
- L-id = https://itunes.apple.com/lookup?id=<id>&country=cn
- Apple US 打脑壳 = https://podcasts.apple.com/us/podcast/id1706779447
- X-pid = https://www.xiaoyuzhoufm.com/podcast/<pid>, with the pids exactly as cited in the briefing
- NE = https://music.163.com/djradio?id=1379007
- NE-API = https://music.163.com/api/dj/program/byradio?radioId=1379007&limit=600&offset=0&asc=true
- SP = https://open.spotify.com/show/54xYojKlgvmAyisRsfnCUP
- YT = https://www.youtube.com/feeds/videos.xml?playlist_id=PLhUDXwq1_-HO9EnEMaTxWEjtLf3Ckjl-g
- HF = https://huggingface.co/datasets/MagicHub/chuan-yu-12-city-sub-dialect-speech-dataset
- PW = https://podwise.ai/blog/xyzfm-and-podwise
- RH = https://github.com/DIYgod/RSSHub/tree/master/lib/routes/xiaoyuzhou (source read at raw.githubusercontent.com/DIYgod/RSSHub/master/lib/routes/xiaoyuzhou/podcast.ts)
- App Store lookups (country=us), by app id: 小宇宙 1488894313, 喜马拉雅FM 876336838, NetEase 590338362, Bilibili 1517062289, Himalaya 1275493456
- App Store pages: https://apps.apple.com/us/app/id<app id>

| # | claim (short) | cited source | verdict | evidence (quote, URL) |
|---|---|---|---|---|
| 1 | 野地电波 "一个说四川话的猎奇向电台"; host DDTea | feed; Apple | STATED | YD description: "一个说四川话的猎奇向电台，可能是你正在寻找的那个，来扎起！"; author DDTea. Same text on A-1648306891; L-1648306891 artistName DDTea. |
| 2 | 196 episodes | feed; Apple | STATED | YD has 196 items; L-1648306891 trackCount 196. |
| 3 | latest 2026-09-22 (54 min), 2026-09-15 (75 min) | feed; Apple | STATED | YD: 欺世录：卖掉埃菲尔铁塔分几步？ 2026-09-22 16:00 GMT, 54:04; 野地怪谈 2026：中秋篇 1:14:54. 16:00 GMT is 00:00 on 23 Sep in China; the briefing uses the feed's GMT date. |
| 4 | "weekly" | feed | STATED (inferred; source states no cadence) | YD dates: 38 episodes in the 365 days to 2026-10-07; of 37 gaps, 26 are 6–7 days, 10 are 13–14, one is 21. |
| 5 | ghost stories, scams, crime, odd histories | feed | STATED | YD titles: 野地怪谈 2026：中秋篇; 欺世录：卖掉埃菲尔铁塔分几步？; 末代贼王; 毒爱故事：莉莉丝的诅咒; description "猎奇向". |
| 6 | "at 55–100 minutes" | feed | SCOPE | YD last 365 days (n=38): min 54.1, median 67.3, max 162.0 min; 31 within 55–100, 5 over 100, 2 just under 55. All-time 0.6–164.3. |
| 7 | Apple search 成都话 returns 32 shows | Apple search | STATED | https://itunes.apple.com/search?term=%E6%88%90%E9%83%BD%E8%AF%9D&media=podcast&entity=podcast&country=cn gives resultCount 32 with 32 results. |
| 8 | "mostly noise: descriptions mention Chengdu … in Putonghua" | Apple search | SCOPE | Read 29 of 32 descriptions (the other 3 are dialect shows): only 4 mention 成都 (海椒Radio, 成都凯爸财富朋友圈, 灵感成都, 那间街角的茶铺). Most hits match 话 in titles or episode text. No description says Putonghua. |
| 9 | 小宇宙 in US App Store; v3.2.0; 2026-09-22 | App Store | STATED | US lookup 1488894313: 小宇宙·一起听播客, version 3.2.0, currentVersionReleaseDate 2026-09-22T04:27:02Z. |
| 10 | Simplified Chinese only | App Store | STATED | https://apps.apple.com/us/app/id1488894313: "Languages: Simplified Chinese". |
| 11 | 喜马拉雅FM in US App Store | App Store | STATED | US lookup 876336838: 喜马拉雅FM（听书社区）电台有声小说相声评书, v9.5.13; page "English and Simplified Chinese". |
| 12 | "(registration by phone number)" | App Store | SCOPE | https://apps.apple.com/us/app/id876336838: no such listing text. Privacy label "Data Linked to You: Contact Info, Phone Number". Only a 2019 review: "I registered and logged in with my phone number". |
| 13 | 网易云音乐 not in US App Store | NetEase lookup | STATED | https://itunes.apple.com/lookup?id=590338362&country=us gives no result; apps.apple.com/us/app/id590338362 returns HTTP 404 (cn returns 200, "网易云音乐-数亿音乐畅听"). |
| 14 | … nor Hong Kong App Store | NetEase lookup (covers US only) | STATED | HK lookup resultCount 0; apps.apple.com/hk/app/id590338362 returns 404; name searches ("网易云音乐", "NetEase Cloud Music") in us and hk list no such app. The cited URL does not cover HK. |
| 15 | Bilibili has an international build | App Store | STATED | https://apps.apple.com/us/app/bilibili-anime-video-hd/id1517062289: "bilibili - Anime · Video HD", seller BILIBILI SINGAPORE PTE. LTD., 13 language codes incl. EN. The phrase "international build" is not used. |
| 16 | 野地电波 "dialect claim is the host's own" | feed | STATED | The 说四川话 line is the channel's own description field (YD). |
| 17 | 摆一哈: two Chengdu women in New York; 13 episodes | 小宇宙 | STATED | X-652852daea568f470958e30b: "由两个旅居纽约多年的成都女孩创立的播客"; episodeCount 13. EP13 notes: hosts now "分别生活在湾区与纽约". |
| 18 | latest "about June 2026" | 小宇宙 | SCOPE | X-652852daea568f470958e30b latestEpisodePubDate 2026-05-29T06:17Z (EP13). |
| 19 | "slow" | 小宇宙 | STATED | Episodes 2025-03-20, 2025-05-12, 2025-08-21, 2026-03-24, 2026-05-29; 131 days since the last. |
| 20 | only E03 labelled "四川话特辑"; show page does not support "mainly dialect" | 小宇宙 | STATED | "E03. 四川话特辑 \| 从中到西：如何选择在哪个国家和文化中生活？"; no other title or the description mentions dialect. |
| 21 | 山城龙门阵: Chongqing; host 豌杂汤; "重庆话方言播客" | 小宇宙; Apple | STATED | author 豌杂汤. Episode notes: "「山城龙门阵」是一档重庆话方言播客" (X-5fe2dd71dee9c1e16de5ebdb, A-1544690700, SC). The phrase is in episode boilerplate, not the show description. |
| 22 | 20 episodes; show notes; 952 subscribers | 小宇宙; Apple | STATED | episodeCount 20; subscriptionCount 952; L-1544690700 trackCount 20; episodes carry notes. |
| 23 | "6–22 min" | 小宇宙; Apple | SCOPE | SC durations 2.1–22.2 min; six under 6 min (2.1, 4.9, 5.2, 5.3, 5.5, 5.5). |
| 24 | last 2023-12-31 | 小宇宙; Apple | STATED (China-local date) | latestEpisodePubDate 2023-12-30T22:00Z = 2023-12-31 06:00 China time. The Apple JSON-LD lists 2023-12-30. |
| 25 | 好生说Radio title and tagline | 小宇宙; Apple | STATED | Title "好生说Radio｜成都方言播客"; description "用成都话，摆巴适龙门阵！这里是《好生说 Radio》". |
| 26 | 56 episodes; 577 subscribers | 小宇宙; Apple | STATED | episodeCount 56 (L-1567932960 trackCount 56); subscriptionCount 577. |
| 27 | "mostly April 2021 to December 2022" | 小宇宙; Apple | SCOPE | HS: oldest item 2021-05-05 (【好生说成华】新华公园电烤羊肉串yyds); 2021:38, 2022:17, last 2022-12-04. |
| 28 | one episode on 2026-05-12 | 小宇宙; Apple | STATED | HS pubDate 2026-05-12 23:10 GMT (13 May 07:10 China time). |
| 29 | 打脑壳 host 打主播Jinji, "apparently Bay Area-based" | Buzzsprout feed | STATED (hedge kept) | DNK author 打主播Jinji. Ep. 13 notes: "上个月打主播在湾区见到了台北市议员苗博雅"; location not stated outright. |
| 30 | "the host speaks only Sichuan dialect and English" | Buzzsprout feed | STATED (translation) | Source is Chinese: "打脑壳播客是一个主播只会说四川话和英语的节目" (DNK, Spotify, Apple US). |
| 31 | 14 episodes, 2023-09-04 to 2025-01-12 | Buzzsprout feed; Apple US | STATED | DNK: 14 numbered episodes (01 on 2023-09-04; 14 on 2025-01-12, feed local PT) plus an un-numbered 2.5-min notice "哦豁，开天窗了" (2024-02-03). Feed and Apple US count 15 items. |
| 32 | "25–135 min" | Buzzsprout feed | SCOPE | DNK durations: ep 10 = 7.3 min, ep 02 about 23, ep 01 = 25.6; max ep 13 = 135.3. |
| 33 | silent about 21 months | Buzzsprout feed | STATED | Newest 2025-01-12; 2026-10-07 is 20.8 months later. |
| 34 | on Apple US, Spotify and YouTube | Buzzsprout feed; Apple US | STATED | DNK description lists Apple Podcasts, Spotify and a YouTube playlist. SP title "打脑壳WordsMisunderstood \| Podcast on Spotify". YT feed has 15 videos, newest 2025-01-13. |
| 35 | topics Bashu society and culture; one Yunnan-dialect episode | Buzzsprout feed | STATED | "关注巴蜀社会和文化从过去到现在的种种"; ep 11 "云南话聊胡杰和陈东楠镜头下的大花苗赞美诗合唱团". |
| 36 | 我爱龙门阵 (25广播) "四川方言类群体脱口秀电台" | feed | STATED | WA: "力求打造最贴心的四川方言类群体脱口秀电台！"; title "25广播 — 《我爱龙门阵》". |
| 37 | 225 episodes; last 2023-08-21 | feed | STATED | WA has 225 items; newest "十年有你 By.我爱龙门阵 2023 Vol.1", 21 Aug 2023. |
| 38 | "main run 2018–2019" | feed | WRONG | WA items span 2013-08-13 to 2019-05-23 plus 2023-08-21. Per year: 2013:30, 2014:39, 2015:41, 2017:56, 2018:50, 2019:8, 2023:1. Only 58 of 225 fall in 2018–2019. |
| 39 | 轻松一刻四川话版: news-comedy digest in Sichuanese; 489 programmes | NetEase | STATED | NE: "原创新闻热点脱口秀《轻松一刻四川话版》"; "共489期" (NE-API count 489). Some are labelled by variety: Vol. 63 南充话版, Vol. 64 成都话版. |
| 40 | "13–18 min" | NetEase | SCOPE | NE-API durations 10.4–32.4 min, median 15.2; 427 of 489 within 13–18; 32 under, 30 over. |
| 41 | "dated from 2015-09 (earliest seen, Vol. 64)" | NetEase | SCOPE | NE-API: Vol. 1 "鸡血人生" 2015-04-24 (free, public); Vol. 64 is 2015-09-10. |
| 42 | "to 2018-10" | NetEase | STATED | Vol. 489 dated 2018-10-16 (lastProgramCreateTime 1539661924926). |
| 43 | 你好，重庆 last 2019-01-19; 重庆龙门阵 2019-08-31; 重庆方言 2021-02-21 | Apple | STATED | Lookup and page dates 2019-01-19T04:37Z, 2019-08-31T06:35Z, 2021-02-21T12:09Z (A-1512882237, A-1512562437, A-1094156352). LZ first item 21 Feb 2021. |
| 44 | 德耒DELAY "about 2022" | 小宇宙 | SCOPE | X-63ba86c4da83c49d996a5ec8: latestEpisodePubDate 2023-01-14T12:17Z; all 11 episodes dated 2023-01-08 to 2023-01-14. |
| 45 | 德耒DELAY 35 subscribers | 小宇宙 | STATED | subscriptionCount 35; description "四川话聊天节目". |
| 46 | 四川方言搞笑 clip dump, 2024-04-21 | Apple | STATED | L-1778441029 releaseDate 2024-04-21T11:30Z. FY: 213 items of 0.4–6 min titled "更新 (n)"; description "四川方言搞笑". |
| 47 | 龙门阵罪话: narrator "用方言", Hangzhou co-host in Putonghua | feed | STATED | LMZ: "洋芋，在重庆用方言带你进现场。桑尼，在杭州用普通话帮你拆解谜团。" |
| 48 | 8 episodes 2026-03-23 to 2026-05-10, none since | feed | STATED | LMZ has 8 items: E1 23 Mar 2026 to E8 10 May 2026 (22:00 GMT); nothing later. |
| 49 | 海椒Radio hosts 老韩 and 小曹 (Chengdu) | feed | STATED | HJ notes: "主播：老韩、小曹"; description "在成都，聚一下，喝两口，聊几句。" |
| 50 | "an episode every one to three months" | feed | STATED (approx.) | HJ last 12 months: 7 episodes, gaps 27–71 days. 2025 had a 194-day gap (Vol.084 2025-04-30 to Vol.085 2025-11-10). |
| 51 | Vol. 091 on 2026-08-27; dialect not stated | feed | STATED | "Vol.091 中元节特辑2026！" 27 Aug 2026 00:30 GMT. No dialect statement in the description; only Vol.078 is about 成都话. |
| 52 | 洋芋摆巴适: 784 episodes; last 2023-11-10; feed does not say dialect | feed | STATED | YY has 784 items; newest 10 Nov 2023; description "洋芋摆巴适，给你摆点儿老实龙门阵"; no 四川话, 方言 or 脱口秀 anywhere in the feed. |
| 53 | 府河小茶铺 "19,941 subscribers" | 小宇宙 | SCOPE | X-643fb7c39361a4e7c3f4ae59 subscriptionCount 19951 (read twice); live counter. |
| 54 | Sichuan-based hosts; language not stated | 小宇宙 | STATED | The three podcasters' profiles carry ipLoc "四川"; brief "新晋罪案博客，女子侦探团"; no language statement. Evidence is profile IP location, not page text. |
| 55 | 摆龙门阵 / 架势说 / 亚龙阵 descriptions only explain the phrase | 小宇宙 | STATED (note) | 摆龙门阵: "摆龙门阵，在四川话中的大意为大家聚在一起闲谈，聊天。" 亚龙阵: "“摆龙门阵”在川渝方言里是聊天、唠嗑的意思。" 架势说: "“架势说”源自四川话，意思同just talk" (explains its own title; still no dialect-show claim). |
| 56 | HF dataset: 12 cities, 33 hours, Putonghua transcripts, open | Hugging Face | STATED | HF README: "Total: 33 hours / 13,068 utterances / 38 native speakers"; 12 cities listed; "Standard Mandarin transcription"; "open-source Chinese dialect speech dataset". |
| 57 | "its licence is unverified" | Hugging Face | SCOPE | HF README front matter: "license: cc-by-4.0". The repo holds only README.md; data download is at magichub.com. |
| 58 | 打脑壳 (dormant), the one clearly Sichuanese show on Apple US, Spotify, YouTube | Spotify | STATED | SP page exists; latest episode "14. 草堂读书会：08年前后的四川公民社会一窥｜和杨雨摆龙门阵". The Apple US 四川话 search lists no other live Sichuanese show. |
| 59 | Apple US lists 轻松一刻四川话版 and 你好，重庆, long-dead | Apple US search | STATED | https://itunes.apple.com/search?term=%E5%9B%9B%E5%B7%9D%E8%AF%9D&media=podcast&entity=podcast&country=us gives resultCount 2: 你好，重庆（重庆话四川方言）last 2019-01-19; 轻松一刻四川话版 last 2017-04-08. |
| 60 | English "Sichuanese" searches return food and China-topic shows | Apple US search | STATED | term=Sichuanese&country=us gives 49 results, e.g. Salt & Spine, Sinica Podcast, Eater's Digest, The China Travel Podcast, Mandarin Blueprint; no dialect show. The cited URL is the 四川话 query, so this is a separate query. |
| 61 | Many shows on RSS hosts (Buzzsprout, Lizhi, Ximalaya, 小宇宙); feeds work in any podcast app | Podwise; RSSHub; feed | STATED | Apple feedUrls: rss.buzzsprout.com (打脑壳), rss.lizhi.fm (重庆方言), ximalaya.com/album (野地电波 etc.), feed.xyzfm.space (海椒Radio). Enclosures returned HTTP 206 (one 野地电波 request reset once, then fine). 你好，重庆 uses papi.qingting.fm, not in the list. |
| 62 | 小宇宙 hosting exposes feeds at feed.xyzfm.space/<id> | Podwise; feed | STATED (by the feeds, not Podwise) | LMZ and HJ link to xiaoyuzhoufm.com with ?utm_source=rss, copyright "@小宇宙App". PW never mentions feed.xyzfm.space. |
| 63 | fetched fine from outside China; Ximalaya feeds readable | feed | STATED | Reproduced from this sandbox (location unknown): HTTP 200 and valid RSS for HJ and the Ximalaya feeds. |
| 64 | 小宇宙 shows without a feed can be followed via RSSHub; 2023-12 | Podwise; RSSHub | STATED | RH route `/xiaoyuzhou/podcast/:id` exists. PW (Dec 1, 2023): "Podwise 导入小宇宙节目时，背后也是通过 RSSHub 来获取 RSS 链接的。" The route reads only the episodes embedded in the show page (about the newest 15). |
| 65 | "a third-party route that may be rate-limited" | RSSHub; Podwise | NOT IN SOURCE | Neither PW nor the route source mentions rate limits. The hedge is the briefing's own. |
| 66 | Himalaya "is the international edition of Ximalaya" | App Store | SCOPE | https://apps.apple.com/us/app/himalaya-audiobooks-podcasts/id1275493456: "Himalaya, a brainchild of Ximalaya 喜马拉雅, is an inspirational content app"; seller Himalaya Media Inc. |
| 67 | Himalaya "holds audiobooks and English courses, not Sichuanese podcasts" | App Store | SCOPE | Same listing: "featuring short audio courses and motivational stories". What's-new: "Trending screen adaptations, BL audio dramas, and fun children's encyclopedia stories". "Audiobooks" appears only in the app title; no "English" and no Sichuanese content mentioned. |
| 68 | App Store listings don't say whether a Chinese phone number is needed (Unknown) | App Store | STATED | Neither the 小宇宙 nor the 喜马拉雅FM listing says. One 喜马拉雅FM review says paid channels were not accessible "being outside China". |
| 69 | "guessed Play URLs returned 404" (Unknown) | none cited | STATED | Reproduced: play.google.com/store/apps/details?id=app.podcast.cosmos, com.ximalaya.ting.android and com.ximalaya.ting.lite all return HTTP 404. A 404 on guessed package IDs does not prove absence. |
| 70 | Ximalaya web pages are JavaScript-only (Sources) | none cited | STATED | https://www.ximalaya.com/album/33132000 returns a shell ("Loading interface…") with no show content in the HTML. |

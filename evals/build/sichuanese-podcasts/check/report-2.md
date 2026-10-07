# Agent 2 report: press, video platforms and reference works

**The report file was not written.** The Write tool refused: "Subagents should return findings as text, not write report files". Nothing was appended to `report-2.md` and I created no other file. The full table is below, so please save it if you want the file. Checked 2026-10-07, about 95 tool calls.

## Counts

59 atomic claims checked, 1 not checkable. Counts are by row; row 35 covers seven words, all STATED.

| Verdict | Rows |
|---|---|
| STATED | 41 |
| SCOPE | 11 (7 of them minor) |
| WRONG | 3 |
| NOT IN SOURCE | 4 |
| SUPERSEDED | 0 |

Row 52 (李伯清 on Douyin) is a declared unknown. My search found nothing either. No claim in my group was left unreached. Agent 1's claims were not touched.

## Non-STATED rows with one-line fixes

- **R1 SCOPE (minor).** en.Wikipedia says he "decided to be a Buddhist monk" in October 2007. Write "decided to become", not "became".
- **R6 SCOPE (minor).** 大话水浒 ep. 41–70 ran 23:40 to 36:22, not 23–35. They came with gaps, and there were none after 2025-12-14. Write "23–36 min" and "near-daily until 2025-12-14".
- **R7 SCOPE (minor).** YouTube shows only "2.39K subscribers". Write "about 2,390".
- **R8 SCOPE (minor).** The 大话水浒 episodes on YouTube run 25:45 to 37:19, and the earlier 成都发财梦 series ran 13–23 min. Write "about 26–37 min".
- **R15 NOT IN SOURCE.** No source compares sizes, and the briefing's own list has bigger or comparable bodies. Drop "largest" or compute hours.
- **R18a NOT IN SOURCE.** The iQiyi page is a user playlist (播单) with a blank creator, uploaded through a 爱奇艺号 account. Drop "Official".
- **R18c WRONG.** The page and iQiyi's own data show no VIP marker. Write "no VIP flag seen".
- **R22b NOT IN SOURCE.** The Bilibili search API gives names, follower counts and bios, not spoken language. Reword as "not assessed" or cite a listening.
- **R24 SCOPE.** en.Wikipedia lists the Chengdu 1st tone as both 55 and 45, and Wiktionary says it is "closer to 45". Reword: all sources give 55 or 45 for tone 1. The two cited English URLs also redirect.
- **R33 SCOPE.** The "after tone 2 or 4 → tone 1" rule is stated only for reduplicated words (爸爸, 婆婆). Other compounds "in many cases" go to tone 1, with no tone condition.
- **R34 SCOPE.** The source's rule is that 儿 takes tone 1 after a tone-2 syllable (娃儿 ua²ɚ¹), not that erhua "appears after tone 2".
- **R36 SCOPE (minor).** "仅有两点主要区别" is Wikipedia's own sentence. 蓝勇 1997 is cited only for the 听感 clause. Write "Chinese Wikipedia says".
- **R41 SCOPE (minor).** Only the 宜宾 title names the town taught. The other two pages give the creator's hometown. Write "creators from 邛崃 / 遂宁".
- **R42b NOT IN SOURCE.** Neither the page nor its metadata gives the teaching language. Drop "taught in Putonghua" or mark it as inferred. The title has no colon: 乡音计划《四川成都话入门100句》.
- **R44b SCOPE.** The notes label guests 英国中, 德国中 and 爱尔兰中 and say they give Sichuanese self-introductions. "Overseas Sichuanese" is an inference. Write "guests based in the UK, Germany and Ireland".
- **R45b WRONG.** There are 12 terms under 方言科普 DIALECT BREAKDOWN, plus 2 tongue twisters. The "13" in the show text is the number of interview questions (在13个提问中). Many terms are 巴中 speech.
- **R47 SCOPE (minor).** The page covers the Chengdu-Chongqing dialect, and the three dictionaries are listed only under References.
- **R53 WRONG (Bilibili half).** The official Bilibili account has posted only twice since 2025-12-14 (2025-12-31 and 2026-10-07). Only YouTube is daily, and the fan channel posts every 3 days. Fix the Log line.

## Full table

| # | claim (short) | cited source | verdict | evidence (quote, URL) |
|---|---|---|---|---|
| 1 | en.Wikipedia says 李伯清 became a Buddhist monk in 2007, nothing later | en.wikipedia Li_Boqing | SCOPE (minor) | "In October 2007, Li Boqing decided to be a Buddhist monk in Sanmei Temple in Pengzhou County." It also says he would keep doing charity shows. Nothing dated after 2007. https://en.wikipedia.org/w/index.php?title=Li_Boqing&action=raw |
| 2 | He is 79 | 川观新闻 7428198 | STATED | "演出前，79岁的李伯清在后台接受川观新闻记者采访时". Page stamped 2026-03-27. en.Wikipedia says born February 1947, so he is 79 until Feb 2027. https://cbgc.scol.com.cn/news/7428198 |
| 3 | Nanxi, Yibin stop on 2026-03-27 was his third of the year | 川观新闻 7428198 | STATED | "宜宾站是李伯清今年公益巡演的第三站，也是他时隔十年再次来到南溪。" Also "3月27日下午…宜宾站在南溪区南溪古街举行". Stamp 2026-03-27 22:54. https://cbgc.scol.com.cn/news/7428198 |
| 4 | Bilibili account labelled official has 136,858 followers | space.bilibili.com/2082464890 | STATED | The card API gives name 李伯清散打评书, fans 136,860 on 2026-10-07 (live count, +2). Official title "李伯清散打评书官方账号", 214 videos. https://api.bilibili.com/x/web-interface/card?mid=2082464890 |
| 5 | Posted 2026-10-07, and before that 2025-12-31 | Bilibili | STATED | Uploads: 2026-10-07 14:04, then 2025-12-31 18:34 (0:57), then 大话水浒第70集 on 2025-12-14. https://api.bilibili.com/x/series/recArchivesByKeywords?mid=2082464890&keywords=&ps=40&pn=1 |
| 6 | After daily 大话水浒 (23–35 min) in Nov–Dec 2025 | Bilibili | SCOPE (minor) | 30 episodes (ep. 41–70) from 2025-11-04 to 12-14. Durations 1420–2182 s, i.e. 23:40–36:22. No uploads on 11-17 to 11-19 or 12-02 to 12-09, and none after 12-14. Same URL as R5. |
| 7 | YouTube channel calls itself official, 2,390 subscribers | YouTube UCA20z… | SCOPE (minor) | Description: "【李伯清散打评书】官方频道。" The page shows "2.39K subscribers" and "335 videos", rounded, not exact. https://www.youtube.com/channel/UCA20zLJB1lBVo0QWdet1qTA |
| 8 | Posts near-daily 28–35 min episodes | YouTube | SCOPE (minor) | The Atom feed shows one upload a day from 2026-09-23 to 10-07 (大話水滸 五–十九). Channel-page durations for 大話水滸 一–十九 run 25:45–37:19 (e.g. 35:45, 37:19). https://www.youtube.com/feeds/videos.xml?channel_id=UCA20zLJB1lBVo0QWdet1qTA |
| 9 | 《傻儿师长》 premiered on Tencent Video on 2026-02-11 | 川观新闻 7270368, 封面, NetEase | STATED | 川观 (2026-02-09): "新版《傻儿师长》将于2月11日起在腾讯视频全网独播". NetEase (2026-02-12): "《傻儿师长》也在腾讯视频上线了". 封面 names no platform. https://cbgc.scol.com.cn/news/7270368 |
| 10 | 22 episodes of 35 minutes | 封面新闻 (news.qq.com) | STATED | "新版《傻儿师长》共22集，每集35分钟。" 川观 has no count or runtime. https://news.qq.com/rain/a/20260209A06Z1N00 |
| 11 | "全方言演绎" | 封面新闻 | STATED | "为真实展现川渝特色，该剧不仅全方言演绎". Not in 川观. Same URL as R10. |
| 12 | 李伯清 as chief planner | NetEase (not 川观 or 封面) | STATED | "新版《傻儿师长》由李伯清担任总策划，还在剧中扮演樊老太爷。" This is the author's own text in a 网易号 post. 川观 and 封面 do not say it. maigoo.com also lists "总策划兼主演李伯清". https://c.m.163.com/news/a/KLIFEMCS0556BNC0.html |
| 13 | 李伯清 is in the cast | 封面 / 川观 | STATED | 封面: "在剧中饰演“樊老爷”的著名散打评书艺术家李伯清". 川观: "主演廖健、李伯清携主演向甜…集体亮相". https://news.qq.com/rain/a/20260209A06Z1N00 |
| 14 | A NetEase outlet says some actors' dialect is "不正宗" | NetEase | STATED | "有些方言还说得不正宗，整体来看，比老版差多了". It is the author's own text, from the 网易号 account 后世的君子, 2026-02-12. The source is a self-media account, and it says "some dialect", not "some actors'". https://c.m.163.com/news/a/KLIFEMCS0556BNC0.html |
| 15 | 李伯清's episodes are the largest body of dialect audio found | none ("above") | NOT IN SOURCE | No source compares sizes. Counts seen: Bilibili official 214 videos, fan channel 145, YouTube 335. The briefing lists 洋芋摆巴适 at 784 episodes, 轻松一刻四川话版 at 489, and 野地电波 at 196 × 55–100 min. |
| 16 | Fan channel re-uploads about one ~28 min piece every 3 days | space.bilibili.com/97176612 | STATED | Uploads at 08:00 on 2026-09-01, 09-04, … 10-07, each 1670–1768 s (27:50–29:28), e.g. "【李伯清評書】梅花香自苦寒来！". In Aug 2026 it posted 3–6 min segments twice a day. The channel is 李伯清評書专场, 756 followers, unverified. Nothing on the page about provenance or licence. https://api.bilibili.com/x/series/recArchivesByKeywords?mid=97176612&keywords=&ps=30&pn=1 |
| 17 | Official on Bilibili: 《王保长新篇》, 26 episodes, first free | Bilibili ss24032 | STATED | PGC API: total 26, ep. 1 status 2 (free), ep. 2–26 status 13 (会员), copyright "bilibili". https://api.bilibili.com/pgc/view/web/season?season_id=24032 |
| 18a | 《山城棒棒军2（方言版）》 is official on iQiyi | iQiyi playlist1833510502 | NOT IN SOURCE | The page is a 播单 with a blank 创建视频 field. Items come from uploader_id 1567039014 via "ugc_openapi_mp_iqiyi", "qiyiProduced":false, uploaded 2018-10. https://www.iqiyi.com/playlist1833510502.html |
| 18b | 32 episodes | iQiyi | STATED | Header "视频数：32". Only 29 are in the page data (08, 15, 25 absent). Same URL. |
| 18c | VIP | iQiyi | WRONG | All 29 items have "payMarkUrl":"" (a VIP title in iQiyi's list API carries a vip_*.png), "payMark":0, and the player API gives bossStatus 0 and vipType "". The page has no VIP label. Logged-out view, not played. https://pcw-api.iqiyi.com/video/video/playervideoinfo?tvid=25291895909 |
| 19 | 《傻儿师长》(1992), 《傻儿司令》 and 《雾都夜话》 not in Bilibili's licensed catalog | cited pages do not cover it | STATED | `search/all/v2`: the media_bangumi and media_ft groups are empty for all three. The control 王保长新篇 returns ss24032 and ss21430. https://api.bilibili.com/x/web-interface/search/all/v2?keyword=傻儿师长 |
| 20 | 《傻儿师长》 and 《傻儿司令》 appear only as fan re-uploads | Bilibili video search | STATED | User uploads only: "傻儿师长(1992)DVD原盘1080p渲染修复" by 大朴的小朴 (2025-06-30) and "傻儿司令【超清修复版】四川方言无删减 25集全" by 墨沫略萌. "May disappear" is a judgement. https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword=傻儿司令 |
| 21 | 四川话配音 documentaries on Bilibili behind VIP: 《川味》 s3, s4 and 《川味之乡厨》 | ss26637, ss39867, ss41081 | STATED | Titles "川味 第三季（四川话配音）", "川味 第四季（四川话配音）", "川味之乡厨（四川话配音）". All full episodes are status 13 会员. ss39867 also has 7 free 预告 trailers. https://api.bilibili.com/pgc/view/web/season?season_id=39867 |
| 22a | 敬汉卿, 冷水煮乐器, 托马斯家的, 活蹦乱跳的肥曈 are big creators | Bilibili search API | STATED | Followers: 9,125,720; 1,383,105; 1,435,402; 1,509,124. https://api.bilibili.com/x/web-interface/search/type?search_type=bili_user&keyword=敬汉卿 |
| 22b | They are mainly Mandarin with Sichuan flavour | Bilibili search API | NOT IN SOURCE | The API returns names, followers and bios only. The bios say nothing about language. Same URL. |
| 23 | Sichuanese ASMR and sleep-aid channels exist, mostly roleplay | Bilibili search API | STATED | Search "四川话 助眠" returns 229 results, led by 碎碎冰月亮 "【四川话助眠】…角色扮演｜情景模拟" (450,021 plays). The exception is 冬瓜盈耳汤 "四川话Vlog". https://api.bilibili.com/x/web-interface/search/type?search_type=video&keyword=四川话 助眠 |
| 24 | en.Wikipedia and Wiktionary give 1st 55, 2nd 21, 3rd 53, 4th 213 | en.wikipedia, Wiktionary | SCOPE | Wiktionary: "The actual pronunciation of the first tone is closer to ˦˥ (45) in Chengdu." en.Wikipedia's Chengdu row lists the 1st tone as "55" and "45" (Li Rong 1998), then 21, 53, 213. Both cited URLs redirect. https://en.wikipedia.org/wiki/Sichuanese_dialects and https://en.wiktionary.org/wiki/Wiktionary:Chinese_entry_guidelines/Sichuanese |
| 25 | zh.Wikipedia gives 1st 45 and 3rd 42 | zh 四川话 | STATED | Chengdu row: 45 / 21 / 42 / 213, 入声归入阳平. The zh 成都话 page agrees: "阴平、阳平、上声、去声的调值分别为45, 21, 42, 13". https://zh.wikipedia.org/wiki/四川话 |
| 26 | Another Wikipedia page gives a 2nd tone of 31 | en Chengdu-Chongqing dialect | STATED | Chengdu row: 55 / 31 / 53 / 213. Chongqing: 55 / 21 / 42 / 214. https://en.wikipedia.org/wiki/Chengdu-Chongqing_dialect |
| 27 | Wiktionary: 213 becomes a low rise (13) in flowing speech | Wiktionary | STATED | "In flowing speech, the fourth tone (213) becomes a low rising tone ˩˧ (13)." https://en.wiktionary.org/wiki/Wiktionary:Chinese_entry_guidelines/Sichuanese |
| 28 | Wikipedia pages agree the entering tone merges into the 2nd | en, zh, en CC | STATED | en Sichuanese dialects, Chengdu and Chongqing: "merged into the 2nd". zh: "成都话入派阳平". Wiktionary: "in Chengdu and Chongqing it has merged with the second tone". The en CC page lists four tones and does not say it in words. |
| 29 | No retroflex initials: 祖 = 主 | zh 成都话 | STATED | "不分ts與tʂ，…祖=主"; "没有[ʈʂ]…等翘舌音的声母". https://zh.wikipedia.org/wiki/成都话 |
| 30 | n/l merge before open vowels: 纳 = 辣 | zh 成都话 | STATED | "泥母來母洪音混，細音不混 / 納=辣". The source term is 洪音, i.e. finals without i/y, which also covers u. "Open vowels" is a loose gloss, but the example is exact. Same URL. |
| 31 | -in/-ing and -en/-eng merge: 因 = 英 | zh 成都话 | STATED | "不区分[ən]和[ɤŋ]，[in]和[iŋ]这两对韵母。比如，“森”和“僧”、“因”和“英”同音。" Same URL. |
| 32 | 我 and 硬 start with [ŋ] | zh 成都话 | STATED | "“硬”读做/ŋən/，“我”读作/ŋo/". Same URL. |
| 33 | After tone 2 or 4 the 2nd syllable of a compound often goes to tone 1 (爸爸, 婆婆) | en Chengdu-Chongqing dialect | SCOPE | "The first type involves reduplicated words: … the second character changes to the dark level tone (1st tone)." For other compounds it says only "In many cases, the 2nd character's tone changes into the 1st tone". https://en.wikipedia.org/wiki/Chengdu-Chongqing_dialect |
| 34 | Erhua appears after tone 2 (娃儿) | same | SCOPE | "If there is one character before the 儿 and it has the 2nd tone, the 儿 character changes to the 1st tone." The rule is the tone of 儿 (娃儿 ua²ɚ¹). Same URL. |
| 35 | Core words: 巴适, 耙耳朵, 雄起, 要得, 老子, 不存在, 嘛, 嗦 | en.wikipedia; The World of Chinese (2018-11-02) | STATED | en.Wikipedia: 雄起 "to cheer someone on", 耙耳朵 "henpecked husbands", 巴适 vs 好. TWoC: "要得 (Yáode) means “OK,”"; "老子 (Lǎozi) is an arrogant way to refer to oneself"; 不存在 "no problem"; "嘛 ( Ma ) indicates suggestion or agreement"; "嗦 ( So ) expresses suspicion or dissatisfaction". 雄起 appears only in en.Wikipedia. https://www.theworldofchinese.com/2018/11/fangyan-friday-3-the-rap-of-sichuanese/ |
| 36 | A source quoted on zh.Wikipedia: big difference by ear, yet "仅有两点主要区别" | zh 重庆话 | SCOPE (minor) | "虽然重庆话与…成都话在听感上拥有较大差异，但音韵上除少数例外字外，仅有两点主要区别。" It is Wikipedia's own sentence. 蓝勇 1997 is cited on the 听感 clause only, and 钟维克 2005 after the second point. The rules are stated for 川东 dialects, with Chongqing as representative. https://zh.wikipedia.org/wiki/重庆话 |
| 37 | Chongqing has no [ȵ]; those words go to [l]; n/l merge before i | zh 重庆话 | STATED | "没有聲母/ȵ/…重庆话中声母都归并入/l/…导致声母l与n“洪混细也混”". Same URL. |
| 38 | Some words end in [yu] where Chengdu has [yo] | zh 重庆话 | STATED | "在成都话中部分韵母为/yo/的通摄入声字…在重庆话等川东方言中韵母为/yu/". Same URL. |
| 39 | Chongqing tones 55/21/42/214 | zh 重庆话 | STATED | "调值依次为55、21、42和214". Same URL. |
| 40 | Academic "Chongqing speech" = main urban area, about a fifth of the population | zh 重庆话 | STATED | "学术上所指的重庆话，仅仅只是重庆市主城区的语言，使用人口约占重庆全市人口的五分之一。" Same URL. |
| 41 | Several "learn Sichuanese" videos teach 邛崃, 宜宾 or 遂宁 speech | BV1Sp4y1r7sj, BV1qJ411T7VH, BV1wu411Z7un | SCOPE (minor) | 宜宾: title "学四川话 宜宾话 老城区 最常用句子200句". 邛崃: description "邛崃话考试猜对了几句？". 遂宁: "我是313号 来自四川遂宁". Only the 宜宾 title names the town taught. https://www.bilibili.com/video/BV1wu411Z7un/ |
| 42a | 《乡音计划》 video uploaded 2023-08-06, about 30,000 views | BV1k94y1C7K9 | STATED | pubdate 2023-08-06 20:02, view 30,182, duration 3:23. Title 乡音计划《四川成都话入门100句》. https://www.bilibili.com/video/BV1k94y1C7K9/ |
| 42b | Taught in Putonghua | same | NOT IN SOURCE | Description: "欢迎大家和我一起学习成都话~". No subtitles listed, and the page does not state the teaching language. |
| 43 | 100种生活 episode: 73 min, 牧老师 and 杜老师 (host of 野地电波), timestamps, published 2025-05-26 | 小宇宙 68339d3a… | STATED | Title "爱好特辑｜四川话有多巴适，你听了这期就晓得！". pubDate 2025-05-25T22:30Z (= 05-26 Beijing), 4352 s (page shows 73分钟). Notes: "杜老师（播客《野地电波》）", "00:00 开场介绍…". The page does not say "host". https://www.xiaoyuzhoufm.com/episode/68339d3a40ebba808209483f |
| 44a | 废物没有假期 Vol. 38, 80 min, "practical Sichuan dialect guide", about 2024-02 | 小宇宙 65deefbe… | STATED | Title "Vol.38【成都】超实用四川话指南…". pubDate 2024-02-28, 4818 s (80.3 min). https://www.xiaoyuzhoufm.com/episode/65deefbe9bf20df4c86e102b |
| 44b | …with overseas Sichuanese guests | same | SCOPE | Notes: "嘉宾：夏叶、阿基、罗老师（英国中）、子威（德国中）、MOUMOU（爱尔兰中)" and "来听听嘉宾们的四川话自我介绍吧". Neither "overseas" nor "Sichuanese origin" is stated. |
| 45a | BreadToast episode "四川，我们来啦!" for English speakers, show notes, about 2020 | 小宇宙 5f1313ae… | STATED | Title "南腔北调 #4 – 四川，我们来啦! - Sichuan Dialect Pt. 1". pubDate 2020-07-18, 32 min, bilingual notes. https://www.xiaoyuzhoufm.com/episode/5f1313ae6d76607427f1abc7 |
| 45b | …with a 13-term breakdown | same | WRONG | 12 entries under "方言科普 DIALECT BREAKDOWN" (gua … 巴适得拌), plus 2 tongue twisters. The "13" is "在13个提问中探寻…". |
| 46 | $1.99 iOS app "Sichuanese - Chinese Dialect" (Chengdu, human audio, English meanings), updated 2025-07 | App Store id1490232242 | STATED | US storefront. "REAL HUMAN VOICE Including the alphabet, words."; "The dialect of Chengdu, the capital of Sichuan province"; Version 1.2, 07/22/2025. https://apps.apple.com/app/id1490232242 |
| 47 | Wiktionary "Sichuanese Pinyin" for Chengdu, from three dictionaries (1986–98) | Wiktionary | SCOPE (minor) | "Wiktionary uses the Sichuanese Pinyin to transcribe the Chengdu-Chongqing dialect of Sichuanese". References: 《成都方言詞典》 (1998), 《成都话方言词典》 (1987), 《四川方言词典》 (1986). No statement that the romanization derives from them. |
| 48 | 2026-02-07 Sichuan Daily commentary says "孩子只学说普通话" | 川观新闻 7263785 | STATED | "越来越多家庭中，孩子只学说普通话，四川话正从代际传承中褪色。" Published 2026-02-07 18:05, footer 四川日报报业集团. The quote carries the qualifier "越来越多家庭中". https://cbgc.scol.com.cn/news/7263785 |
| 49 | en.Wikipedia: since the 1980s–90s young people's Sichuanese is greatly influenced by the national language | en.wikipedia | STATED | Fluency reduced "since the 1980s and 1990s": "The Sichuanese spoken by them is greatly influenced by the national language." https://en.wikipedia.org/wiki/Sichuanese_dialects |
| 50 | 傻儿师长 episode count: news says 22, a snippet said 21 | Unknown section | STATED | 封面 and Sina: 22 episodes. maigoo: "集数：21集" and elsewhere "延长至24集"; TVMaze (crowd-sourced): 21. A 24 figure also exists. VIP gating still unverified. https://m.maigoo.com/citiao/1285196.html |
| 51 | Bilibili catalog carries area_limit = 316 | Unknown section | STATED | `rights.area_limit` is 316 on ss24032, ss26637, ss39867 and ss41081. |
| 52 | 李伯清 livestreams on Douyin (unknown) | none | n/a | Declared unknown. A web search found no Douyin account or stream. |
| 53 | Log: 李伯清 has near-daily uploads on Bilibili and YouTube | Log | WRONG (Bilibili half) | The official Bilibili account has posted only 2025-12-31 and 2026-10-07 since 大话水浒 ep. 70 on 2025-12-14. YouTube is daily. The fan channel posts every 3 days. R5 and the body of the briefing already say this. |
| 54 | Log: 《傻儿师长》 rebooted in 2026-02 | Log | STATED | See R9 and R12. |

## Method and caveats

- **Wikipedia and Wiktionary** were read as raw wikitext through curl, not as model digests.
- **Press pages** were read through WebFetch, with verbatim quotes requested. Key lines were fetched twice (川观 7428198 and 7263785, 封面, and NetEase for 总策划 and 不正宗), and the NetEase body-versus-comment question was checked. curl to c.m.163.com was reset.
- **Bilibili:** the PGC, card, `recArchivesByKeywords` and `search/all/v2` endpoints work through curl. They need browser-like headers (`Origin`, `Sec-Fetch-*`); without them the API answers 412, and space/wbi endpoints answer -352.
- **YouTube:** durations come from the channel page's thumbnail badges, matched by order. Watch pages return LOGIN_REQUIRED.
- **iQiyi:** the VIP verdict rests on iQiyi's own embedded JSON and player API, from a logged-out session. I did not play the videos.
- **Spam:** search results included spam `*.it.com` domains. I did not use them.

Sources used from web search: https://m.maigoo.com/citiao/1285196.html, https://www.tvmaze.com/shows/90075, https://news.sina.cn/2026-02-09/detail-inhmfuma1956388.d.html?vt=4

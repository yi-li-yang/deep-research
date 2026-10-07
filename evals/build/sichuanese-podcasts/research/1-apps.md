# Agent 1 notes: Chinese podcast apps (Sichuanese / Chongqing dialect)

Started 2026-10-07. Format: claim — source (URL) — date. Status tags: [VERIFIED-primary] = read on the platform's own page/API; [LEAD] = only seen in a search/listing, dialect claim not yet checked; [SHAKY] = contested or promotional.

## Method notes
- itunes.apple.com Search API (country=cn) works through WebFetch (returns JSON summarised by a small model; I asked for raw fields). Raw curl to itunes.apple.com gets 403 from the sandbox proxy, so not used. Values below are as relayed by WebFetch; re-check the important ones on the Apple/xiaoyuzhou page.
- Apple "releaseDate" = date of latest episode in the feed; "trackCount" = number of episodes. Both as of 2026-10-07 fetch.
- Apple search matches show descriptions, so most hits for 成都话 are noise (not dialect shows).

## A. Apple Podcasts CN catalogue (iTunes Search API, fetched 2026-10-07)
Query 四川话 -> 2 results; 四川方言 -> 2; 重庆话 -> 1; 成都话 -> 32 (mostly noise); 方言 -> 18 (many other dialects); 打脑壳 -> 1.

Explicitly Sichuan/Chongqing-dialect-labelled titles on Apple CN:
- 好生说Radio｜成都方言播客 — host 二仙桥欧德李 — 56 eps — latest ep 2026-05-12 — genre 幽默对谈 — feed = ximalaya album 47203982 — https://podcasts.apple.com/cn/podcast/%E5%A5%BD%E7%94%9F%E8%AF%B4radio-%E6%88%90%E9%83%BD%E6%96%B9%E8%A8%80%E6%92%AD%E5%AE%A2/id1567932960 (a second duplicate listing id1589593279) — Apple API 2026-10-07 — [LEAD: need to check activity after May 2026 and language mix]
- 四川方言搞笑 — 只爱好声音 — 213 eps — latest ep 2024-04-21 — genre 即兴表演 — ximalaya album 78481728 — https://podcasts.apple.com/cn/podcast/%E5%9B%9B%E5%B7%9D%E6%96%B9%E8%A8%80%E6%90%9E%E7%AC%91/id1778441029 — Apple API 2026-10-07 — [LEAD; apparently inactive since 2024-04 on Apple]
- 你好，重庆（重庆话四川方言） — 68互联 — 100 eps — latest 2019-01-19 — 纪实 — qingting feed — id1512882237 — STOPPED (2019)
- 重庆龙门阵 — 68互联 — 93 eps — latest 2019-08-31 — 纪实 — ximalaya album 7072601 — id1512562437 — STOPPED (2019)
- 重庆方言 — 重庆方言 — 40 eps — latest 2021-02-21 — 喜剧 — lizhi 612841 — id1094156352 — STOPPED (2021)
- 轻松一刻四川话版 — 网易轻松一刻 — 257 eps — latest 2017-04-08 — 喜剧 — ximalaya album 395373 — id990576038 — STOPPED (2017); a Sichuanese-dialect version of NetEase's 轻松一刻 news-comedy digest
- 半打脑壳 — Zac — 4 eps — latest 2022-07-21 — xyzfm feed — id1633076173 — tiny, inactive since 2022 [LEAD]

Other leads surfaced by 成都话 search (dialect use NOT yet checked; may be noise):
- 海椒Radio (two Apple listings: lizhi 48652601, 91 eps, latest 2026-07-30; 韩老人 xyzfm feed, 91 eps, latest 2026-08-27)
- 肥话连篇 — 肥杰 — 244 eps — latest 2026-08-16 — ximalaya 56109512
- 松果白话 — 217 eps — latest 2026-10-07 — lizhi 293345907 — 犯罪纪实
- 鲶鱼夜话 — 298 eps — latest 2026-09-21 — ximalaya 66572833 — 犯罪纪实
- 半夜谈MNT — 谈谈谈哥 — 22 eps — latest 2025-08-27 — xyzfm
- 山下夜话 — shanxiaguo — 203 eps — latest 2026-08-25 — xyzfm
- 灵感成都 — 17 eps — latest 2023-07-18 — xyzfm
- 青年度日指南 — 446 eps — latest 2026-09-30 — ximalaya 33454990
- 体制内｜小职员们的聊天局 — 繁繁&雪锋 — 201 eps — latest 2026-09-28 — ximalaya 70278366
- FM435190 (lizhi 435190, comedy, 2000 eps, latest 2026-07-08)
- 那间街角的茶铺：从成都茶铺看大众文化城市生活历史 — 多云下的蛋 — 182 eps — latest 2024-05-04 — probably Putonghua, about Chengdu teahouses
- 方言夜读 — 华语环球广播 — 100 eps — latest 2024-06-05 (multi-dialect reading? check whether any Sichuanese)

## B. Web search leads
- A search result summary says 「打脑壳」 is a podcast whose host speaks only Sichuanese and English, about Bashu society/culture, on 小宇宙/Apple/Spotify/YouTube with RSS. Source was a search-engine summary only, NOT yet verified on a primary page. [LEAD]. Note Apple CN search for 打脑壳 returned only 半打脑壳 (different show, 4 eps); 打脑壳 itself may be listed on a non-CN storefront or only on 小宇宙.

## C. VERIFIED on primary pages/feeds (2026-10-07)

### 打脑壳 WordsMisunderstood  [VERIFIED-primary, feed read]
- Host 打主播Jinji (Apple "artist" field), feed https://rss.buzzsprout.com/2243225.rss (Buzzsprout; show page wordsmisunderstood.buzzsprout.com/2243225). Apple US page: https://podcasts.apple.com/us/podcast/%E6%89%93%E8%84%91%E5%A3%B3wordsmisunderstood/id1706779447 (NOT found in the CN storefront search; the CN search for 打脑壳 only returned the unrelated 半打脑壳). Genre on Apple US: Society & Culture.
- Channel description (feed, English as written by the show): "A program where the host speaks only Sichuan dialect and English, focusing on Bashu society and culture from past to present." (self-description, not independent confirmation.)
- 15 items incl. a 147-second "哦豁，开天窗了" notice; numbered episodes 01-14. First ep 2023-09-04 ("01. 四川话讲严歌苓新书《米拉蒂》（上）"); latest ep 14 on 2025-01-12 (Apple releaseDate 2025-01-13T04:00Z) ("草堂读书会：08年前后的四川公民社会一窥｜和杨雨摆龙门阵", 4755 s = ~79 min). So NO new episode for ~21 months as of 2026-10-07 -> effectively dormant/stopped (cannot rule out a hiatus).
- Format: mostly host solo (单口) or 1-guest 摆龙门阵 interviews, 25-135 min (several >1 h; ep13 8120 s = 135 min). Topics: books/film/documentaries, Bashu dialect comedy history (ep05 巴蜀喜剧兴衰考略：春晚、李伯清、中江表妹和假老练; ep08 谐剧/王永梭), LGBTQ in Sichuan (ep04, ep12), Taiwan politics (ep07), civil society. Politically sensitive social topics; overseas-oriented (ep10 screenings in SF Bay Area/LA/Tokyo). Ep11 is in Yunnan dialect ("云南话聊...") so language is not 100% Sichuanese.
- Learner view: authentic, unscripted Sichuanese by a (probably overseas-based) host who also uses English; no transcripts seen in feed (not checked on show page). Titles in Putonghua/Chinese characters with dialect words (e.g. 为啥子, 摆龙门阵, 啥子) — good for lexicon, but long and topic-heavy.

### 好生说Radio｜成都方言播客  [VERIFIED-primary: Apple page + RSS]
- Host 二仙桥欧德李 (feed says three hosts). Apple CN page: https://podcasts.apple.com/cn/podcast/%E5%A5%BD%E7%94%9F%E8%AF%B4radio-%E6%88%90%E9%83%BD%E6%96%B9%E8%A8%80%E6%92%AD%E5%AE%A2/id1567932960 ; feed http://www.ximalaya.com/album/47203982.xml (Ximalaya-hosted).
- Apple description (Chinese, raw): "用成都话，摆巴适龙门阵！...不聊宏大叙事，只讲身边的烟火气，吐槽“成堵 city”的早晚高峰，分享三色路路冲的快乐，听开店老板讲创业的酸甜苦辣，唠唠老成都过年的老规矩；也带你穿越古蜀文明的千年时光..." Category 幽默对谈 (humorous chat). Rated 5.0 from 2 ratings (tiny audience signal).
- Episode record: first batch April-June 2021 (district-by-district series 【好生说锦江/青羊/成华/金牛/高新/天府/武侯】 plus short segments 【筛边打网】 12-17 min), many eps through 2022 (Apple lists 17 Jul 2022, 31 Jul, 7 Aug, 28 Aug, 16 Oct, 23 Oct, 4 Dec 2022), then a GAP, then ONE episode on Tue 2026-05-12 ("从三十七郡县之一到蜀汉都城，这些年是怎么过来的", 27 min; Apple displays it as "May 12" with no year = current year). Apple trackCount 56 (feed ~53-56). Episodes usually 40-65 min.
- Status: stopped 2022-12-04, one-off revival 2026-05-12. "Active in 2026" is shaky: one episode in 9 months. [SHAKY]
- Language: Chengdu dialect throughout per own description; heavy English code-mixing in titles (chill, city, local, CDC=成堵city joke).

## D. Tooling notes
- Ximalaya web pages are JS-only (WebFetch returns only footer) and the web API needs a token (ret 407 "webtk缺失"). BUT Ximalaya RSS feeds (http://www.ximalaya.com/album/<id>.xml) are readable and give item dates. Use them for Ximalaya-hosted shows.
- Apple podcasts.apple.com pages ARE readable via WebFetch (description, ratings, recent eps).
- WebFetch summaries of very long feeds are unreliable on date order (the first summary of the 好生说 feed mislabelled newest/oldest); cross-check with Apple page/API.

## E. Feed/page checks of Apple 成都话-search leads (2026-10-07) — mostly NOISE
- 四川方言搞笑 — 只爱好声音 — ximalaya album 78481728 — feed description is just "四川方言搞笑"; items titled "更新 (N)" of 1-6 min each, dated 2024-02-15 to 2024-04-21 (feed has >100 items; Apple trackCount 213) — looks like a clip dump, not a produced show; last item 2024-04-21 -> STOPPED. [low quality, only title claims dialect]
- 肥话连篇 — 肥杰 + 惠子 — ximalaya 56109512 / Apple id1603580035 — weekly relationship/life chat, VOL.243 on 2026-08-16 (1h33), 4.4/5 from 7,285 Apple ratings (large audience). Last item 2026-08-23 "没有我们的日子里大家也要认真生活哦～" (6 min) = hiatus announcement. Neither feed nor Apple page mentions 四川话/成都话/方言 -> NO evidence it is dialect; probably noise. [dialect UNCONFIRMED]
- 鲶鱼夜话 (ximalaya 66572833; Ep306 2026-09-24, ~1 h, strange-stories) and 松果白话 (lizhi 293345907; daily true-crime, ep 219 on 2026-10-07; "白话" = plain speech) — no dialect statement; Mandarin; noise.
- 半夜谈MNT (谈谈谈哥; last 2025-08-27; true crime) — no dialect mention; noise.
- 山下夜话 (shanxiaguo; Apple lists 210 eps; recent 2026-07/08) — the 四川 mention is only inside one episode blurb about a regional slang word; not a dialect show; noise. (NB: WebFetch summary printed the year as 2024; the 2026-08-25 API timestamp and an ep title about the 2026 World Cup indicate 2026. Summaries can garble years; trust raw API timestamps.)
- 海椒Radio — host 韩老人 — Apple id1652808757 (xyzfm feed) — tagline "在成都，聚一下，喝两口，聊几句。" — category 休闲, 4.5/5 (8 ratings). Eps roughly monthly: Vol.087 2026-02-16, Vol.088 04-29, Vol.089 07-02 (2h31), Vol.090 07-30, Vol.091 中元节特辑 2026-08-27 (1h17). ACTIVE in 2026. Chengdu-based; whether spoken in Chengdu dialect is NOT stated on the Apple page. [LEAD: dialect unconfirmed]

## F. 小宇宙 (Xiaoyuzhou) pages — fetched 2026-10-07 (WebFetch of xiaoyuzhoufm.com/podcast/<id> works; gives subscribers + relative dates; relative dates are coarse)
Site-restricted web search (allowed_domains xiaoyuzhoufm.com) found these:
- 好生说Radio｜成都方言播客 — https://www.xiaoyuzhoufm.com/podcast/6117727a8525166fddaf9069 — host shown as 热心市民老李 (search snippet: residents 爆眼子, 勾勾, 老李) — 577 subscribers — latest ep "5 months ago" (= 2026-05-12, 27 min), previous eps "4 years ago" (2022). Confirms Apple finding: stopped 2022, one-off ep May 2026. Description says "用成都话，摆巴适龙门阵！".
- 德耒DELAY — https://www.xiaoyuzhoufm.com/podcast/63ba86c4da83c49d996a5ec8 — hosts mermer (from Deyang, Sichuan) + 耒王peco (Leiyang, Hunan) (+ bulgogi listed) — described as a Sichuan-dialect chat show (search snippet: started Nov 2019, speaking only Sichuanese) — 35 subscribers — eps 001-011, 29-92 min, latest "4 years ago" -> STOPPED (~2022). Tiny.
- 摆龙门阵 — https://www.xiaoyuzhoufm.com/podcast/61c2a8252d223855ed0af678 — hosts 茄宝, 18宝 — 211 subscribers — 12 eps (#12 "恭喜🎉 距好心态大人又近一步", 21 min, "2 years ago" = ~2024), STOPPED. Description only EXPLAINS the term ("摆龙门阵，在四川话中的大意为大家聚在一起闲谈，聊天。这档播客试图还原朋友间日常对话的轻松自在，并试图找到一点诗意。") — it does NOT say the show is in dialect. [dialect UNCONFIRMED; one WebFetch summary over-read the description]
- 架势说JUST TALK — https://www.xiaoyuzhoufm.com/podcast/64a9484fc1a771dfd679a33c — hosts 泛泛huii, ming君明, 无关紧要的Peter — 124 subscribers — Vol.1-18, 37-144 min; latest Vol.18 "除夕前夜谈" "2 years ago" (~Feb 2024) -> STOPPED. Description: ""架势说"源自四川话，意思同just talk，就是聊天，摆龙门阵！" — again explains the name only. Episode topics are Chengdu-centred (vol17 成都找工作有点具体). [dialect UNCONFIRMED]
- More 小宇宙 hits to check: 吃一嘴 (podcast/64686b846752b5f9de9d361a; snippet: friends dining+chat, Chongzhou/Chengdu dialect is the selling point), 摆一哈 Barely Talk (two Chengdu women in New York; snippet says mainly Sichuan dialect), 南腔北调 (episode/5f1313ae6d76607427f1abc7), 山城龙门阵 (Chongqing; ep17 当我们在说“重庆”时，说的到底是哪里？, ep19 沉浸式烹饪：重庆辣子鸡), 是时候说 (番外篇·龙门阵之川渝拉踩实录; mixed), 亚龙阵 (solo monologue), 锵锵100分钟了 (#85 川渝婚恋挤压问题 成都线下录制), 100种生活 (爱好特辑｜四川话有多巴适 — an ep about the dialect), 饭桌上的家, 高考假期备忘录, 转圈时间, KITE RADIO风筝店播.

## G. 小宇宙 follow-ups (fetched 2026-10-07)
- 山城龙门阵 — https://www.xiaoyuzhoufm.com/podcast/5fe2dd71dee9c1e16de5ebdb — host 豌杂汤 — 952 subscribers — page text quoted by fetch: "「山城龙门阵」是一档重庆话方言播客" (self-description) + "在重庆爬坡上坎的一路上，...在山城，卡卡角角都是龙门阵，大事小事都可以龙门阵。" — EP.01-EP.20; episodes SHORT (6-22 min); topics: Chongqing place names, 冰粉, 鸡公煲, 铜梁龙舞, 辣子鸡 cooking, New Year. Latest EP.20 "该如何告别2023，迎接2024？" (6 min; shown as "3 years ago", i.e. ~end 2023/early 2024); EP.17 dated 2023-07-11 (from earliest comment timestamp, so approximate). => Chongqing dialect, STOPPED after EP.20 (~Jan 2024). Show notes exist (EP17 notes cite scholarly sources on Chongqing's administrative history, mention "Chongqing dialect expressions"). Also listed on Apple, Ximalaya, NetEase, QQ Music per search snippet. BEST LEARNER-FRIENDLY FIND so far: short, scripted-feeling topic episodes with notes, Chongqing speech. [Exact episode dates not obtained; Apple page not yet checked]
- 吃一嘴 — https://www.xiaoyuzhoufm.com/podcast/64686b846752b5f9de9d361a — host 况泽灵 — 4 subscribers — ONE episode EP001 "四个崇州人的酒后闲聊 | 关于ChatGPT、理财等" (76 min, "3 years ago" ~2023). Description (raw): "记录几朋友的饭局聊天节目，以方言（崇州话、成都话）谈话为主打卖点。" -> dialect (Chongzhou/Chengdu), dead and tiny.
- 摆一哈 Barely Talk — https://www.xiaoyuzhoufm.com/podcast/652852daea568f470958e30b — hosts 雪鹅, 草莽 (+小冯 on E03) — two Chengdu women in New York (designer + journalist) — 154 subscribers — 13 eps; EP13 "我们给纽约和回国，都列了一张“离开前”必做清单" 58 min "4 months ago" (~Jun 2026) -> ACTIVE-ish in 2026 (slow: EP12 6 months ago, EP11 1 yr ago). Only E03 is labelled "四川话特辑" (52 min, "从中到西：如何选择在哪个国家和文化中生活？") so the rest is presumably Putonghua; a search-engine summary that said the show is "primarily Sichuan dialect" is NOT supported by the show page. [MOSTLY MANDARIN + 1 dialect special]
- 是时候说 — https://xiaoyuzhoufm.com/podcast/604dc93d393439a08720c4b3 — hosts Sally, 维恩, 凡君 — lifestyle/subculture talk; the one bonus episode 番外篇·龙门阵之川渝拉踩实录 (42 min, "5 years ago" ~2021) notes say: "本期全部内容由大部分四川话和极小部分普通话构成"; show notes include timestamps ("论成都话口音的精髓"). The show itself is not a dialect show. [single dialect episode]
- 亚龙阵 — https://www.xiaoyuzhoufm.com/podcast/624a191fdb4823929e668fd9 — host 亚菁 — 43 subscribers — 15 eps, 3-18 min solo improv monologues; latest "得罪" (5 min, "1 year ago") ; description only glosses 摆龙门阵 as 川渝方言 for chatting -> language of delivery UNCONFIRMED.
- BreadToast Chinese 面包吐思 — https://www.xiaoyuzhoufm.com/podcast/5e4ff2dd418a84a04695e52d — host Brad Johnson (面包/张浩哲), Chinese-learning podcast for English speakers — 204 subscribers — Season 3 series 《南腔北调》 on dialects: #1 北儿京儿话儿 (33 min), #2 北京话 (45), #3 蓝鲸话 (39), #4 "四川，我们来啦! - Sichuan Dialect Pt. 1" (32 min; "6 years ago" ~2020; guests: three native speakers from different Sichuan areas now in Chengdu, interviewed with a 7-year-old child reporter; show notes have time markers, tongue twisters and a 13-term dialect breakdown) -> https://www.xiaoyuzhoufm.com/episode/5f1313ae6d76607427f1abc7 . Learner-oriented; bilingual; 1-2 episodes only. Show last updated "4 years ago".
- 锵锵100分钟了 — https://www.xiaoyuzhoufm.com/podcast/65bda213513a776b57ef2c0c — #85 "日常喷空「川渝婚恋挤压问题」成都线下录制4个半小时完整版" published 2024-11-07 (recorded Oct 19), 273 min, recorded in a Chengdu bar; page does NOT state dialect; commenters mention 重庆话. [UNCONFIRMED]

## H. Site-restricted searches on other platforms (search-engine snippets only, NOT yet verified on pages)
- Ximalaya: 《志说四川方言》 (series by 四川省地方志 + Sichuan Normal University linguists per snippet; eps incl. 第10集 四川方言童谣, 第16集 宜宾话; URL https://m.ximalaya.com/lishi/30297937/241250242 ) — educational, not a podcast chat; 《洋芋摆巴适》 (雨轩&洋洋, "stand-up comedy in authentic Sichuan dialect conversation"); 小刚方言 (Sichuan-dialect stand-up); 四川方言百科; 四川方言（四川话很好懂）. Dialect claims from search snippets only.
- NetEase Cloud Music: 轻松一刻四川话版 radio (492 programmes on NetEase vs 257 on Apple; Chengdu-dialect reading of NetEase's daily digest; Apple feed ended 2017-04-08) — need latest date; 午睡了 (小午睡; Sichuanese cover songs, not a podcast).
- Lizhi: 巴蜀传统文化广播; 跟宇宙结婚 (https://www.lizhi.fm/user/13905815; snippet claims "full Sichuan dialect entertainment-news chat"); dialect label page https://www.lizhi.fm/label/24229966469669424/

## I. More verification (2026-10-07)

### Apple API (country=cn) exact latest-episode dates
- 山城龙门阵 — 豌杂汤 — 20 eps — latest 2023-12-30T22:00Z (= 2023-12-31 Beijing) — genre 个人日记 — feed ximalaya album 44160859 — https://podcasts.apple.com/cn/podcast/%E5%B1%B1%E5%9F%8E%E9%BE%99%E9%97%A8%E9%98%B5/id1544690700 -> STOPPED after EP.20 (31 Dec 2023). Show created on 小宇宙 ~2020-12 (ID timestamp) so ran ~3 years.
- 马上开摆 — 牧老师 — Apple: 57 eps, latest 2026-04-27 (Apple copy lags; feed below has vol 51 on 2026-09-20) — id1642686770.
- 野地电波 — DDTea — 196 eps — latest 2026-09-22T16:00Z — Apple genre 科幻小说 — ximalaya album 33132000 — id1648306891. (A second unrelated show 野的电波 by 野生植物, 1 ep, 2021.)
- 府河小茶铺 has two Apple shows: 小茶铺|悬疑案件 (142 eps, latest 2026-10-03T16:00Z, crime; ximalaya 75921613) and 小茶铺|真资格龙门阵 (34 eps, latest 2026-08-29; chat; ximalaya 76051663).
- 摆一哈 Barely Talk — Apple: 11 eps, latest 2026-03-24 (Apple copy lags the 小宇宙 page, which shows 13 eps) — id1712355016 — ximalaya album 78690369.

### 野地电波 (Ye Di Dian Bo)  [VERIFIED feed + Apple; best "active + actually Sichuanese" candidate]
- Author DDTea (= 杜老师 in the 100种生活 special, who is credited there as host of 《野地电波》; guest of Sichuan-dialect episode 2025-05). Feed: http://www.ximalaya.com/album/33132000.xml (also on Apple id1648306891).
- Channel description (raw, in feed): "一个说四川话的猎奇向电台，可能是你正在寻找的那个，来扎起！" = "a Sichuan-dialect oddities/curiosities radio". Self-description, so the dialect claim is the host's own, not independently measured.
- 196 episodes (Apple). Weekly on Tuesdays. Latest episodes (feed, GMT dates): 2026-09-22 "欺世录：卖掉埃菲尔铁塔分几步？" 54 min; 2026-09-15 "野地怪谈 2026：中秋篇" 75 min; 2026-09-08 "末代贼王" 62 min; 2026-08-25 "野地怪谈2026：中元纳凉特辑" 103 min; 2026-08-18 《娑婆诃》：龙与蛇的量子纠缠; 2026-08-11 毒爱故事：莉莉丝的诅咒; 2026-07-28 控制·Ⅱ; 2026-07-21 逃出恶魔岛 (Escape from Alcatraz). Genre: ghost stories (怪谈), scams, crime and odd histories, told as long (55-100 min) narrated episodes. ACTIVE in 2026 (latest 2026-09-22/23).
- Learner view: narrated storytelling (monologue-ish) with a clear topic, titles in Putonghua; the host is invited as a Sichuanese-speaking guest elsewhere. No transcript seen. Unknown pace. Not yet checked: 小宇宙 page (subscribers), show notes.

### 马上开摆 (牧老师)  [feed read; dialect NOT indicated]
- Feed https://feed.xyzfm.space/4dx7qbf6x3mr (小宇宙-hosted). Description: travel/observation podcast; "这里摆的不是烂,而是龙门阵" — plays on 摆龙门阵. Fetch summary: "No indication the show is spoken in 四川话". 51 items (vol 33 on 2023-07-23 is the earliest in the part read; show began 2022-08-25). Recent: vol 51 2026-09-20 (3h12m, Germany trip), vol 50 2026-04-27 (奄美大岛), vol 49 2026-01-08, vol 48 2025-11-23, vol 47 2025-07-17, vol 46 2025-03-26. Roughly every 2-4 months. Host is named in the 100种生活 Sichuan-dialect special as a Sichuan podcaster. [dialect of the show itself UNCONFIRMED -> treat as probably Putonghua with Sichuan host]

### 府河小茶铺 (Fuhe Little Teahouse)  [language NOT stated]
- 小宇宙 page https://www.xiaoyuzhoufm.com/podcast/643fb7c39361a4e7c3f4ae59 — hosts 太阳, 三土, 贝贝 (白白 on one ep) — 19,941 subscribers (large) — crime/odd-case show; latest ep "长兴'4.20'案" (4 days before 2026-10-07 = ~2026-10-03), weekly. Description does not state a dialect. The one-off episode "神了，四川人！" (2024-04-28 by ID/comment; 50 min) discusses Sichuan people and dialects across regions. Feed for the side show 小茶铺|真资格龙门阵: https://www.ximalaya.com/album/76051663.xml, a casual chat show (Dec 2024 - 2026-09-26), no dialect statement. [Sichuan-based hosts, spoken language UNCONFIRMED]

### 100种生活 special (dialect-focused episode)  [VERIFIED page]
- 爱好特辑｜四川话有多巴适，你听了这期就晓得！ — https://www.xiaoyuzhoufm.com/episode/68339d3a40ebba808209483f — host Sijia with Sichuan podcasters 牧老师 (《马上开摆》) and 杜老师 (《野地电波》) — 73 min — date: page shows 2025-05-26 (recorded 2025-02-24) — show notes with timestamps: Luzhou / Jiangyang / Chengdu variation, 叠词文化 (reduplication), 李伯清, cuisine debates, worries about transmission. "heavily conducted in and about Sichuan dialect" (fetch summary). Good listen for learners wanting explanations of the dialect in a mix of Putonghua and Sichuanese; timestamps help.

### 废物没有假期 Vol.38 【成都】超实用四川话指南，美食到景点，教你把朋友耍称展
- https://www.xiaoyuzhoufm.com/episode/65deefbe9bf20df4c86e102b — show https://www.xiaoyuzhoufm.com/podcast/62065d864baddcbc4cbc133e (host 贝卡; travel talk) — 80 min — ID timestamp 2024-02-28 (page "3 years ago" is rounded) — guests 夏叶, 阿基, 罗老师 (UK), 子威 (Germany), MOUMOU (Ireland) i.e. overseas Sichuanese; fetch summary: mostly Sichuanese with code-switching to Mandarin; "practical Sichuan dialect guide" (food, sights, dating terms, insults, transport announcements). One-off episode in a general travel show. [LEARNER-RELEVANT; overseas guests]

### NetEase Cloud Music radio 轻松一刻四川话版  [VERIFIED radio page]
- https://music.163.com/djradio?id=1379007 — host 网易每日轻松一刻 — 489 programmes, 6,046 subscribers — category 脱口秀 — description "原创新闻热点脱口秀《轻松一刻四川话版》，川味够正不？" (said to air on NetEase News and 南充广播) — first ep seen 2015-09-01 (Vol.64), last eps 487-489 dated 2018-10-16 -> STOPPED Oct 2018. News-comedy digest in Sichuan dialect, ~13-18 min each; a clear learner-friendly format (short, topical) but old.

### Not Sichuanese / noise confirmed
- Lizhi 跟宇宙结婚 (https://www.lizhi.fm/user/13905815): 536 eps, hosts 小伙子/青年/刀夫, general trivia chat, 32,000 followers; NO dialect (a search snippet had wrongly implied Sichuanese).
- 别样人生 (https://www.xiaoyuzhoufm.com/podcast/65ea7d2cdd8f5335b1ae8a17; 洋子 + 小聪明; 521 subs; EP66 about 1 month ago): chat show; only EP58 was a Sichuan-dialect special.
- 朋嗑儿 Vol.93 方言小集锦, 喜番调频 vol.138 方言聚一堂, 怡楽播客 618 各地方言小集合: general shows with a one-off dialect-themed episode (multi-dialect), not Sichuanese shows.
- Ximalaya m.ximalaya.com pages and album RSS for 志说四川方言 (30297937) and 19616442 returned nothing readable.

## J. Apple-API keyword enumeration (摆龙门阵 / 龙门阵 / 川渝 / 巴适) and feed checks, 2026-10-07
- 雨轩&洋洋《洋芋摆巴适》 — author 洋芋兄弟 — Apple: 784 eps, latest 2023-11-10 — Ximalaya album 11136143 (feed http://www.ximalaya.com/album/11136143.xml). Feed description (raw): "南腔北调，嬉笑怒骂，却不油嘴滑舌;...洋芋摆巴适，给你摆点儿老实龙门阵。" Topical comedy/commentary, 16-25 min, near-daily in May 2021, twice weekly late 2023 ("洋芋兄弟重出江湖-…" series Oct-Nov 2023); last 2023-11-10 -> DORMANT ~3 yrs. Dialect: feed text does not state it (title/tone use 摆, 巴适); a Ximalaya search snippet called it "authentic Sichuan dialect stand-up" but that is unverified. [dialect UNCONFIRMED from primary text]
- 25广播 — 《我爱龙门阵》 — author 听友2573681 (anonymous Ximalaya account; "25广播" = a small online radio) — Apple 225 eps; feed read shows items 2018-05-22 to 2019-05-23 plus one 2023-08-21 "十年有你 … 2023 Vol.1" (2h02m anniversary) — http://www.ximalaya.com/album/204097.xml — feed description (raw): "力求打造最贴心的四川方言类群体脱口秀电台！" = group talk-show radio in Sichuan dialect. Episodes 26-75 min, includes live recordings. STOPPED (last 2023-08-21; main run 2018-2019). [self-described Sichuanese; amateur group radio]
- 龙门阵罪话 — author 炸洋芋炸洋芋 — feed https://feed.xyzfm.space/el7u3lpqfq7l — 8 eps weekly 2026-03-23 to 2026-05-10 (E8 "屏幕背后的猎手-14个沉默的孩子与一个15年的判决" 40 min; other eps 13-29 min) — crime-case podcast by two women: one in Chongqing narrates "用方言" (description raw: "洋芋，在重庆用方言带你进现场"), the other in Hangzhou uses Putonghua to analyse -> MIXED, built-in Putonghua explanation; ACTIVE in spring 2026 but no episode since 2026-05-10 (~5 months) [stalled?]
- 聊到没电 (85 eps; latest 2026-10-07): working-people chat; no dialect statement; one ep with a Sichuan-Chongqing guest (麻将). Noise.
- Other 龙门阵-titled Apple results with no sign of dialect (title only): 科学声音龙门阵, 健身行业龙门阵, 足球龙门阵, 纯AI龙门阵, 煎饼豆汁儿龙门阵 (Beijing), 屌丝龙门阵, 龙门阵法, 龙门阵 LongTalk (不朽真龙), 摆个龙门阵 (李某某li, 2 eps, 2026-05-26), 百龙门诊. Not checked individually.

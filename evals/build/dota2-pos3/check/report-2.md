# Report 2: media and community sources (checked 2026-10-07, about 70 tool calls)

**The report file was not written.** My Write to `/home/user/deep-research/evals/build/dota2-pos3/check/report-2.md` was refused with "Subagents should return findings as text, not write report files". I did not work around it, so nothing was saved incrementally. The full table is below instead.

## Counts (50 atomic claims)
STATED 38, WRONG 1, SCOPE 9, NOT IN SOURCE 2, SUPERSEDED 0.

No page addressed the reader or tried to instruct. I treated the WebSearch tool's summary text as noise.

## Non-STATED rows with a one-line fix
- **#11 WRONG (L22), "(region not stated; his account ID wasn't recorded)":** the cited post says "a 7k (rank ~4k EU) offlane-exclusive player". Fix: write "he says rank ~4k EU; OpenDota gives no region" and record account ID 130676269.
- **#3 NOT IN SOURCE (L21), date 2026-07-30:** neither Hotspawn nor Fragster gives the day (both are dated 31 July). Valve's patch list timestamps 7.41e at 2026-07-30T07:00Z. No fix if Valve's page (Agent 1) carries it.
- **#50 NOT IN SOURCE (L88), "高分局" video where a commenter showed a top rank of 5,200:** no URL is cited and I could not locate it. Fix: give the video URL or drop the 5,200.
- **#8 SCOPE (L73), "whether Immortal Draft still exists":** Hotspawn has a section headed "Immortal Draft Still Exists". Fix: say it existed as of 31 July and that no later source was found.
- **#22 SCOPE (L47), "Mars is disputed":** no cited commentary rates Mars as strong. Nix puts it in the worst group, and ProTracker shows 44.1% at Immortal despite heavy picks. Fix: say "popular but weak (44.1% win rate, Nix worst group); buffed in 7.41f".
- **#23 SCOPE (L47), "Night Stalker rests on two sources":** among the cited commentary only Nix lists it. Fix: name the second source (Reddit passing mentions only) or say "one tier list".
- **#27 SCOPE (L51), Crystallis "a very good change":** he speaks as a safe-lane player and says it favors offlaners only "a little bit". Fix: add both.
- **#29 SCOPE (L52), "pub players say the safelane still keeps the wave under its tower and pulls the big camp uncontested":** this is one commenter (KayV3eV3e, a 5-point reply). The "7:30" limit is not in the thread. Fix: attribute to that one commenter and move 7:30 to the patch-note citation.
- **#32 SCOPE (L53), "he says he is starting a channel":** the cited post says nothing of the kind. He says "I'm considering making offlane-specific guides", then posted a YouTube video and a text guide. Fix: say "he says he is making offlane guides (text and video)" and cite r/learndota2 1vzcl85 and 1w7ac2o.
- **#34 SCOPE (L55), "within 500 gold of the enemy carry at minute 10 counts as a win":** the post gives this as one example matchup (Earthshaker/Spirit Breaker into Shadow Fiend/Treant). Fix: say "for example, in that matchup".
- **#36 SCOPE (L57), "Never first-phase a hero that is easily countered in lane":** the post says "I will never first phase…" and adds an exception: if you are spamming a hero to learn it, first-phase it. Fix: add the exception and the first-person framing. This also resolves the clash with "play your three heroes every game" (#35).
- **#48 SCOPE (L76), "pub stats from the days after are inflated for Tidehunter":** the article reports only the first hours after release. Fix: say "first hours (Dotabuff)" and mark "days after" as inference.

## Minor notes on STATED rows (no fix needed)
- **#17 Nix list:** "S tier" is the briefing's label; the source says "highest category". It omits a separate "Imba" category (Earth Spirit, Pudge).
- **#19:** only the pick comparison is explicitly "at Immortal".
- **#25 and #26:** both interviewees hedge. 33 adds "but we'll see" and expects to lose lanes again. Collapse says "I don't know" and, asked about his own play, "not really".
- **#40:** "standard answers" is the briefing's word; the top commenter lists what he himself does. A 10-point reply says never leave the lane in the first 5 minutes.
- **#44 Centaur builds:**
  - The rival commenter never says "Helm of the Dominator".
  - sports.ru recommends Dominator then Heart: "Просто покупаем Доминатор… выходим в Тараску".
  - A r/DotA2 comment (7 points) says "centaur are going helm heart rush". That is more support for the Heart side than "no data found" suggests.
- **#45 auras:**
  - The aura claim is carried by r/DotA2 only.
  - r/learndota2 1va1i7n has the reviewer recommending "a crimson guard/shiva or hex".
  - A r/DotA2 comment (1 point) says auras matter at "immortal level".
- **#46 op-ed:** only one figure is explicitly credited to Stratz.
- **Reddit scores** are Arctic Shift snapshots about 1.5 to 2 days after posting (391 is about 2026-08-29; 64 is about 2026-10-03), not live.

## What I found about the "OpenDota rank 4,042" player (u/PlainOldMoose)
- In `r/compDota2` 1ur9y6p and `r/TrueDoTA2` 1ur9zsz (2026-07-08, "7.5k Offlane LF coach") he linked Stratz account **130676269**. He wrote "stuck bouncing between 7k and 7.5k" and offered to pay a coach.
- Query used: `GET https://api.opendota.com/api/players/130676269` on 2026-10-07. It returns `rank_tier` 80 (Immortal) and `leaderboard_rank` **4042**, with `loccountrycode` GB. OpenDota gives no region.
- The official EU leaderboard (`https://www.dota2.com/webapi/ILeaderboard/GetDivisionLeaderboard/v0001?division=europe&leaderboard=0`, posted 2026-10-07T20:13Z) lists "Moose", tag MOOSE, country gb, at rank 3,904. That is a name match only, since the board has no account IDs.
- Ranks past about 4,000 are tied: 1,592 distinct rank values in 5,000 rows, 11 rows at 4,033, 7 at 4,044, none at 4,042.
- He called himself "7k" before the rescale (2026-07-08, "7k and 7.5k") and after it (2026-08-26, 2026-09-04). His number barely moved, so "7k since the rescale" is a weak anchor for what 7,000 now means.
- A pub commenter wrote "I'm playing with top4k players in Europe" (r/DotA2 1vzs1n6, kasimaru, 7 points).
- Side finding on Hotspawn: its author, before the rescale, "was sitting at 8,000 MMR a week ago, putting me at the top 1% of players". Arteezy posted a new MMR of 8,500.

## Other observations
- **Outside my group, for Agent 1:** the EU leaderboard snapshot I fetched has 5,000 rows (max rank 4,997), not the 5,006 in the briefing.
- **Lane-creep change not superseded:** I searched the 7.41a, b, c, d, e and f notes for "lane creep", "7:30" and "meet". Only 7.41 has hits, so the March quotes about the meeting point are not superseded.
- **Valve's page script** (`27928.js`, keys `summerscrub2026_matchmaking_bugfix_1`, `_4`, `_5`, `_6`) matches Hotspawn's changelog lines word for word.

## Claims not reached
- **L88 (#50):** I scanned 139 visible comments on about 40 Bilibili videos with "高分局" in the title and found no 5,200 comment. As a guest, the Bilibili API shows only about 3 comments per video, so it may exist deeper.
- **L85:** "NGA, Zhihu and Tieba were not readable" is not checkable.
- **Agent 1's sources** (dota2.com patch feed, Liquipedia, OpenDota queries, Steam, Perfect World, the EU leaderboard row count) were not checked.

## URL key (used in the table)
- HS-MMR https://www.hotspawn.com/dota2/news/dota-2-mmr-deflation-update
- FR-MMR https://www.fragster.com/dota-2-patch-7-41e-immortal-mmr-reset/
- HS-COL https://www.hotspawn.com/?p=169666 (Collapse interview, dated Mar 30, 2026)
- HS-CRY https://www.hotspawn.com/?p=169277 (Crystallis interview, dated Mar 29, 2026)
- D2-7F https://dota2.ru/articles/68292-lucsie-geroi-doty-v-patce-7-41f-meta-bildy-gajdy/
- D2-TI https://dota2.ru/articles/67054-pocemu-collapse-lucsij-igrok-the-international-2026/
- SPORTS https://cyber.sports.ru/dota2/blogs/3314800.html
- CS-NIX https://www.cybersport.ru/tags/dota-2/nix-nazval-silneishikh-ofleinerov-v-patche-7-41e
- CS-COL https://www.cybersport.ru/tags/dota-2/collapse-nazval-luchshikh-geroyev-na-oflein-v-patche-7-41a-dlya-dota-2
- CS-33 https://www.cybersport.ru/tags/dota-2/33-ob-ofleine-v-patche-7-41-stoyat-liniyu-stalo-proshche-no-rano-ili-pozdno
- CS-TIDE https://www.cybersport.ru/tags/dota-2/populyarnost-tidehunter-i-drow-ranger-v-dota-2-vyrosla-vdvoye-posle-vykhoda
- CS-SIK https://www.cybersport.ru/tags/dota-2/sikle-o-7-41f-na-metu-silno-povliyayet-tak-kak-izmeneniya-v-metovykh-geroyakh
- ESR https://esports.ru/dota-2/articles/luchshie-geroi-nedeli-patcha-7-41f-dota-14-09-20-09/
- R-OFF https://www.reddit.com/r/DotA2/comments/1vzs1n6/
- R-MOOSE https://www.reddit.com/r/learndota2/comments/1vzcl85/
- R-USER https://www.reddit.com/user/PlainOldMoose/comments/1w790b4/what_an_immortal_offlaner_thinks_about_in_the/
- R-LOST https://www.reddit.com/r/DotA2/comments/1wv6ujr/
- R-REV https://www.reddit.com/r/learndota2/comments/1va1i7n/
- BILI https://www.bilibili.com/video/BV1Ychi6TEuQ

Reddit was read through Arctic Shift (`https://arctic-shift.photon-reddit.com/api/posts/ids?ids=<id>` and `.../api/comments/tree?link_id=<id>&limit=500`).

## Table
| # | claim (short) | cited source | verdict | evidence (quote, URL) |
|---|---|---|---|---|
| 1 | L21: Immortal MMR rescaled to 1 to 9,500 | Valve (A1), Hotspawn, Fragster | STATED | Hotspawn: "All players are now between 1 and 9500 MMR." HS-MMR. Fragster: "Every Immortal player now has an MMR between 1 and 9,500" FR-MMR. |
| 2 | L21: done by "patch 7.41e" | Fragster | STATED | Fragster: "Patch 7.41e adjusts every Immortal player's matchmaking rating into a new range between 1 and 9,500 MMR." Hotspawn says only "the Summer Scrub update". |
| 3 | L21: on 2026-07-30 | Hotspawn, Fragster | NOT IN SOURCE (these two) | Both dated 31 July 2026 with no day given (Hotspawn: "Valve has just rolled out the Summer Scrub update"). True elsewhere: Valve patch list has 7.41e at 2026-07-30T07:00Z, https://www.dota2.com/datafeed/patchnoteslist?language=english (Agent 1's source). |
| 4 | L21: "Relative player placement and leaderboard positions are unchanged." | Valve (A1), Hotspawn | STATED | Hotspawn changelog, verbatim: "Relative player placement and leaderboard positions are unchanged." HS-MMR. Fragster: "Relative positions on the regional leaderboards remain unchanged". |
| 5 | L21: Random Draft and Ranked Classic removed | Hotspawn, Fragster | STATED | Hotspawn: "Random Draft and Ranked Classic have been removed from the available Ranked modes." Fragster: "removed Random Draft and Ranked Classic from the available ranked mode pool". |
| 6 | L21, L73: Immortal Draft cutoff "reported as" 8,500 | Hotspawn, Fragster | STATED | Hotspawn: "The cutoff for Immortal Draft is still 8500." Fragster: "The Immortal Draft threshold stays at 8,500 MMR". |
| 7 | L21: before the change top players were reported at 16,000 to 18,000 | Hotspawn, Fragster | STATED (two named players) | Hotspawn: "Quinn has apparently gone from 16,000 MMR to 9,000"; "Satanic become the first player to hit 18,000 MMR last week". Fragster: Satanic "had previously reached the historic 18,000 MMR mark". |
| 8 | L73: "whether Immortal Draft still exists" is unknown | Hotspawn | SCOPE | HS-MMR has a section headed "Immortal Draft Still Exists": "Valve has not done anything about it with this update". Fragster's table lists "Immortal Draft entry 8,500 MMR". Answered as of 31 July. |
| 9 | L22: poster calls himself "7k" after the rescale | r/learndota2 1vzcl85 | STATED | u/PlainOldMoose, 2026-08-26: "I'm Moose, a 7k (rank ~4k EU) offlane-exclusive player." Flair "7k pos3 enjoyer". R-MOOSE. Same user wrote "bouncing between 7k and 7.5k" on 2026-07-08 (pre-rescale). |
| 10 | L22, L53: OpenDota shows him as Immortal at leaderboard rank 4,042 | none cited | STATED (uncited; I reproduced it) | Account 130676269 is from his own Stratz link (r/compDota2 1ur9y6p, 2026-07-08). `GET https://api.opendota.com/api/players/130676269` on 2026-10-07 gives rank_tier 80, leaderboard_rank 4042, loccountrycode GB. No region field. EU board lists "Moose", gb, rank 3,904 (name match only). |
| 11 | L22: "(region not stated; his account ID wasn't recorded)" and "points to the top ~4,000" | r/learndota2 1vzcl85 | WRONG | The cited post states the region: "a 7k (rank ~4k EU) offlane-exclusive player". Account ID is public (130676269). "Top ~4,000" is consistent with his own "~4k EU". Charitable reading: "region not stated" refers to OpenDota, which indeed has none. |
| 12 | L14: first Shrine of Wisdom activation probably 7:00 (pub posts only) | r/DotA2 1vzs1n6 | STATED (hedged) | kasimaru, 7 points, 2026-08-27: "7/14/21 min wisdom is completely forgotten regularly." R-OFF. A pub comment, as the briefing says. |
| 13 | L42: dota2.ru editors, 2026-09-29: Enigma "probably the strongest summoner in the meta" | dota2.ru 68292 | STATED | "Наверное, сильнейший саммонер в мете." Dated "29 сентября 2026, 19:21"; intro "Редакция Dota2.ru собрала самых успешных и популярных персонажей меты". D2-7F |
| 14 | L42: plus Doom and Dragon Knight | dota2.ru 68292 | STATED | Under "Третья позиция — оффлейнеры": 1. Enigma, 2. Doom, 3. Dragon Knight. Intro: they work "и на про-сцене, и в матчмейкинге". D2-7F |
| 15 | L43: sports.ru blog, 2026-09-21, "not a top or a rating": Dark Seer, Largo, Centaur | sports.ru blog 3314800 | STATED | "это не топ и не рейтинг, а актуальная на момент старта патча 7.41f подборка самых метовых героев". Offlaners: Dark Seer, Largo, Centaur Warrunner. datePublished 2026-09-21T18:10+03:00. User blog. SPORTS |
| 16 | L44: Nix 7.41e list dated 2026-08-16 | cybersport.ru | STATED | Dated "16.08.2026 в 12:52"; "Nix назвал сильнейших офлейнеров в патче 7.41e"; streamer's Twitch stream. CS-NIX |
| 17 | L44: top group Centaur, Underlord, Dark Seer, Axe, Night Stalker, Timbersaw, Tidehunter; worst Mars, Visage, Magnus, Bristleback | cybersport.ru | STATED (minor) | "В высшую категорию попали Centaur Warrunner, Underlord, Dark Seer, Axe, Night Stalker, Timbersaw и Tidehunter." "В списке худших оказались Mars, Visage, Magnus и Bristleback." Not "S tier"; omits separate "Имба" category (Earth Spirit, Pudge). |
| 18 | L45: Collapse on 7.41a, 2026-04-07: best matchmaking offlaners Tidehunter, Doom, Primal Beast | cybersport.ru | STATED | "Халилов считает самыми сильными персонажами Tidehunter, Doom и Primal Beast." Dated "07.04.2026 в 16:06"; list "в матчмейкинге … для патча 7.41a". CS-COL |
| 19 | L45: ProTracker at Immortal: Mars picked more than Primal Beast but wins less (44.1% against 51.6%) | cybersport.ru | STATED (minor) | "игроки на рангах Immortal чаще берут Mars. При этом Primal Beast существенно обходит Mars по винрейту — 51,6% против 44,1%." Only the pick comparison is explicitly "at Immortal". CS-COL |
| 20 | L46: TaleKidder, EU carry, "EU 7k ladder" first-person videos; Enigma's ladder win rate "keeps topping", no numbers | Bilibili space 236630139 | STATED | Video 2026-09-21, "7.41f 三号位谜团最优对策 一号位娜迦 欧服7k天梯 第一视角". Description: "谜团在天梯对局中胜率持续登顶的原因很简单" [Enigma's ladder win rate keeps reaching the top; the reason is simple]. Cited URL is the uploader page; claim is in the video description. BILI. Titles carry "一号位" (pos 1) and "欧服7k天梯". |
| 21 | L47: Doom, Centaur, Dark Seer, Largo, Enigma, Axe, Timbersaw each in at least one commentary; Underlord and Tidehunter commentary-only; Brewmaster and Necrophos absent from commentary | cited commentary | STATED (commentary side) | Doom: D2-7F, CS-COL. Centaur: SPORTS, CS-NIX, D2-TI. Dark Seer: SPORTS, CS-NIX, D2-TI. Largo: SPORTS. Enigma: D2-7F. Axe: CS-NIX, D2-TI, ESR. Timbersaw: CS-NIX. Underlord: CS-NIX, D2-TI. Tidehunter: CS-NIX, CS-COL. Brewmaster and Necrophos: none. Pro-data side is Agent 1's. |
| 22 | L47: "Mars is disputed" | Nix, cybersport.ru (Collapse), others | SCOPE | Nix: "В списке худших оказались Mars…". Collapse piece: Mars picked more but 44.1% against 51.6%. D2-TI: Collapse played "всего одна игра на Mars". No cited source rates Mars strong. |
| 23 | L47: "Night Stalker rests on two sources" | cited commentary | SCOPE | Only Nix lists it. Reddit has passing mentions: KayV3eV3e (41 points): "heroes that can gank with minimal items (Slardar, NS)"; PlainOldMoose: "picking slardar / nightstalker is never going to go horribly wrong". Second source not identified. |
| 24 | L47, L87: esports.ru weekly gainers lists, Dota2ProTracker data, filters unstated | esports.ru | STATED | "Топ составлен по данным портала dota2protracker: в список попали герои, которые за прошедшую неделю прибавили в винрейте". No rank or region filter anywhere on the page. A 7.41e weekly page exists too (slug …-24-08-30-08). "Selection effects" is the briefing's judgement. ESR |
| 25 | L51: 33, ESL One Birmingham, 2026-03-27: standing the lane got easier; lane closer to the tower; Jakiro and Warlock slightly nerfed | cybersport.ru | STATED | "Линия появляется ближе к башне, плюс Jakiro и Warlock немного ослабили. Так что стоять линию стало проще, но посмотрим." Dated "27.03.2026 в 00:59". CS-33 |
| 26 | L51: Collapse 2026-03-30: teams "abused" the old start, creeps "met under the tower", patch "fixed the offlane meta" | Hotspawn ?p=169666 | STATED (hedge dropped) | "many teams abused the "moment". Like, with the starting creeps, they met under the tower, so the wave [always] died."; "they just fixed the offlane meta, I would say." Asked about himself: "I mean, not really." HS-COL |
| 27 | L51: Crystallis 2026-03-29: "a very good change", safelane "can start blocking the wave from your base" | Hotspawn ?p=169277 | SCOPE | Quotes verbatim: "I think this is a very good change."; "you can start blocking the wave from your base or something to make it better for yourself." But he speaks as a safe laner and, asked whether it favors offlaners: "It should, a little bit." HS-CRY |
| 28 | L52: thread "Offlane is by far the worst role to play in pubs", r/DotA2, 2026-08-27, 391 points | r/DotA2 1vzs1n6 | STATED | Title exact; posted 2026-08-27T12:04Z by ibra24x; score 391 (snapshot about 2026-08-29), 328 comments. R-OFF |
| 29 | L52: pub players say the safelane still keeps the wave under its tower and pulls the big camp uncontested; change lasts until 7:30 | r/DotA2 1vzs1n6 | SCOPE | One commenter, KayV3eV3e (5 points): "now it takes 0 effort to constantly keep creeps under the safe-lane tower … you can pull big camp from the safe lane uncontested". His 41-point comment says "lane creeps position". OP blames pos 4 and strong safelane duos. "7:30" is not in the thread. R-OFF |
| 30 | L53: u/PlainOldMoose self-declared "7k pos 3" | Reddit user post 1w790b4 | STATED (elsewhere) | Not in the user post (title "What an Immortal Offlaner thinks about in the first 2 minutes"). In R-MOOSE: "a 7k (rank ~4k EU) offlane-exclusive player"; flair "7k pos3 enjoyer". |
| 31 | L53: "no sales found" | Reddit | STATED (negative, consistent) | 2026-07-08: "I am very happy to pay an hourly rate" (he sought a coach). No sales in his 41 posts or 100 latest comments (2026-06-23 to 2026-10-06). |
| 32 | L53: "he says he is starting a channel" | Reddit user post 1w790b4 | SCOPE | Cited post has nothing on a channel. R-MOOSE (2026-08-26): "I'm considering making offlane-specific guides". r/learndota2 1w7ac2o (2026-09-04): "I have produced my first two guides" (YouTube video, text guide). |
| 33 | L54: ask "if all four heroes walk up to the creep wave and fight, who wins?"; sets items, approach, success criterion | Reddit user post | STATED | "you can find out which scenario you are in by asking yourself: if all 4 heroes walk up to the creep wave and fight, who wins?" It dictates items, approach, "What your success criteria is for the lane". He prefaces "In a very oversimplified way". R-USER |
| 34 | L55: in a horror lane, within 500 gold of the enemy carry at minute 10 counts as a win | Reddit user post | SCOPE | "if you as the Offlaner have within 500g of the enemy Carry minute 10, you have successfully survived a horror lane and can consider it a win." Given as "For example" for Earthshaker/Spirit Breaker into Shadow Fiend/Treant. R-USER |
| 35 | L56: pick a pool of three heroes and play them every game | Reddit user post | STATED | "pick 3 heroes (at a time) that you want to learn, and play them in order"; "Pick it every single game". R-USER |
| 36 | L57: never first-phase a hero easily countered in lane | Reddit user post | SCOPE | "I will never first phase a hero that is easily countered in lane". Footnote: "if you are going to spam a hero to learn it, just first phase it". R-USER |
| 37 | L58: let supports' picks constrain yours (ranged partner who won't go in; no stuns) | Reddit user post | STATED | "Your lane partner is a ranged hero that doesn't go in? Now you can't pick heroes that require a melee bruiser to lane". "Your support duo have 0 stuns between them? You cannot pick another hero without a stun". R-USER |
| 38 | L59: don't contest runes if you have no regeneration | Reddit user post | STATED | "DO NOT CONTEST RUNES IF YOU HAVE NO REGEN"; TLDR "Never contest a rune on a no-regen start". Scope: pre-game bounty runes. R-USER |
| 39 | L60: dated 2026-09-04 | Reddit user post | STATED | Created 2026-09-04T16:20Z, 17 points (snapshot). R-USER |
| 40 | L61: top comment 64 points, no flair, 2026-10-01: pull or stack the hard camp; cut waves; or jungle and catch the wave at the tower | r/DotA2 1wv6ujr | STATED | InsidiousSaibot, 64 points, no flair, 2026-10-01T18:22Z: "1st thing is I want to make it so the wave state is near my tower … 2nd is cutting waves … 3rd is just going jungling". R-LOST |
| 41 | L61: others add staying in XP range against a dual lane, and rush boots | r/DotA2 1wv6ujr | STATED | Ferendir_Zero (22): "Stay inside xp range. Most of the time you'll be against a dual lane. Which means they have to split XP while you dont." ariukidding (5): "If you rush boots you can cut the wave". R-LOST |
| 42 | L62: reviewer self-declared 7.5k "pos 3 only", 2026-07-29 | r/learndota2 1va1i7n | STATED | MadMixu, 2026-07-29T18:21Z: "(7.5k mmr, i play only pos 3)". The day before the 07-30 rescale. R-REV |
| 43 | L62: five mistakes (no starting armor on Centaur; chasing the tanky support; returning after enemy level 6; farming away from the team; Heart twice) | r/learndota2 1va1i7n | STATED | "you didnt buy any starting armor for Cent"; "you shouldnt target ogre … better to focus on ark warden"; "After Ark hit lvl 6 you shouldve left the lane and go jungle"; "wounder off somewhere else to farm creeps"; "Getting 2 hearts was a big mistake too". R-REV |
| 44 | L64: Centaur Blink + Blade Mail (reviewer) against Helm into Heart (rival: high ranks "almost always" build Heart second) | r/learndota2 1va1i7n | STATED (minor) | MadMixu: "you shoulve never bought Dominator and instead went for blademail + blink." TestIllustrious7935 (2): "High ranks almost always build Heart 2nd item on Cent currently". He never says Helm. R-REV |
| 45 | L65: two pub players avoid auras ("over hyped"; supports don't stay near the aura carrier); teammates still expect them | r/DotA2 1vzs1n6, r/learndota2 1va1i7n | STATED (r/DotA2 only) | EarnestTriangle (42): "I rarely get aura item offlane. They're over hyped." kasimaru (7): "Supports play on the opposite side of the map from their tankiest aura guy." Specialist-Arm3496 (22): "no matter the hero you are supposed to always get aura items". R-OFF |
| 46 | L67: op-ed, 2026-08-24: offlaner a "punching bag" against easy-lane doubles; stand-the-lane heroes popular; Spirit won with pos 3 as a "third position" | dota2.ru 67054 | STATED | "Оффлейнер в 7.41e — груша для битья, которая приходит против сумасшедшей даблы в легкой: Shadow Fiend, Terrorblade, Undying, Treant Protector, Lifestealer". "Как раз поэтому популярность получили Centaur Warrunner, Dark Seer, Axe и Underlord." "Магомеду пришлось стать настоящей «тройкой»". Dated "24 августа 2026, 07:26". One explicit Stratz figure ("выиграл линию всего 5 раз"). D2-TI |
| 47 | L76: Trove of Terror (night of 6 to 7 October) roughly doubled Tidehunter and Drow Ranger pick rates; cybersport.ru citing Dotabuff, 2026-10-07 | cybersport.ru | STATED | "За несколько часов после релиза частота выбора обоих героев увеличилась примерно вдвое"; "В ночь на 7 октября Valve добавила … Trove of Terror"; "Данные взяты с сайта Dotabuff." Dated "07.10.2026 в 10:44". CS-TIDE |
| 48 | L76: pub stats from the days after are inflated for Tidehunter | cybersport.ru | SCOPE | The article covers only "за несколько часов после релиза" [within hours of release]; no filter stated; nothing on later days. CS-TIDE |
| 49 | L77: Team Spirit analyst, 2026-09-16: 7.41f "very short", will affect the meta strongly | cybersport.ru | STATED | sikle: "Патч очень короткий, но благодарен и за него"; "на мету офк сильно повлияет, т.к изменения в метовых героях сильные." Dated "16.09.2026 в 11:39"; "Аналитик состава Team Spirit". CS-SIK |
| 50 | L88: a Bilibili "高分局" video where a commenter showed the top rank was 5,200 | Bilibili (no URL) | NOT IN SOURCE | Could not locate. Searched about 60 videos titled with "高分局"; read 139 visible comments (guest API shows about 3 per video). No 5,200. Only generic doubts, e.g. BV1jTpw6dEQa: "能放叠油套子也是高分局吗？" and BV15Gh96XEcN: "分段高不高知道，游戏理解不咋样". |

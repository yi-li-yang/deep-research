# Audit: `examples/league-of-legends.md`

Audited 2026-10-06, after the official 26.20 notes went up (about 18:00 UTC). Sources checked: Riot patch notes 26.1–26.20, the Riot patch schedule, Data Dragon 16.19.1, the lolesports primer and Riot news posts, gol.gg tables (parsed directly), and op.gg and lolalytics pages read on Oct 6 (patch 16.19, Emerald+ unless noted). Stats-site numbers move during a patch. Gaps of about 0.1–0.2 points were treated as matching.

**Summary: 132 claims checked. 110 correct, 2 wrong, 5 unverifiable, 15 mis-cited. 2 superseded by the final 26.20 notes, and the final notes changed none of the preview numbers.**

Verdicts: **correct** means a source supports it. **WRONG** means a primary source contradicts it. **unverifiable** means it could be neither confirmed nor refuted. **mis-cited** means it is true, but the source the briefing cites for it does not say so. "Superseded" is an extra tag on top of the verdict.

## Claim-by-claim

| # | Claim (short) | Verdict | Evidence |
|---|---|---|---|
| 1 | 26.19 live Wed Sep 23; 26.20 live Wed Oct 7 | correct | [Riot patch schedule](https://support.riotgames.com/en-us/league-of-legends/gameplay/patch-schedule-league-of-legends/) lists both dates; both are Wednesdays |
| 2 | Riot calls 26.20 the Worlds patch; 26.19 notes say "the Worlds patch (which is the patch *after* this one)" | correct | Exact sentence is in the [26.19 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-19-notes/). The [26.20 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-20-notes/) intro: "it's time for WORLDS!" |
| 3 | Next patches: 26.21 Oct 21, 26.22 Nov 4, 26.23 Nov 18, 26.24 Dec 9 | correct | [Riot patch schedule](https://support.riotgames.com/en-us/league-of-legends/gameplay/patch-schedule-league-of-legends/) |
| 4 | Client and Data Dragon say 16.19.1; pro sites use 16.x (16.17 = 26.17) | correct | First entry in [versions.json](https://ddragon.leagueoflegends.com/api/versions.json) is "16.19.1"; the gol.gg patch column shows 16.16/16.17 |
| 5 | 26.20 notes unpublished as of 17:39 UTC; Riot posts about 18:00 UTC the day before | correct · **superseded** | True when written. The [26.20 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-20-notes/) are now out (Oct 6) |
| 6 | Mid-patch updates are rare: only 26.1, 26.3, 26.6 and 26.9 had one in 2026 | **WRONG** | 26.10 also had one, a Smolder micropatch. See the [26.10 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-10-notes/) "Update:" and [Phroxzon](https://x.com/RiotPhroxzon/status/2055079979239825743): "We just pushed a micropatch nerf to Smolder" |
| 7 | 26.19 is Riot's "first round of pro-focused" changes | correct | Verbatim in the [26.19 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-19-notes/) |
| 8 | 26.19 buffs: Aatrox, Aphelios, Aurora, Draven, Elise, Fiora, Kha'Zix, Lillia (R 2→2.5s), Volibear | correct | 26.19 notes; Lillia R duration 2 ⇒ 2.5s |
| 9 | 26.19 Lucian reshaped to rely less on enchanters | correct | 26.19 notes: Vigilance on-hit 15 (+20% AD) ⇒ 5 (+15% AD), Q base damage up. [Phroxzon](https://x.com/RiotPhroxzon/status/2104800631001415990): enchanter pairings "received a large nerf as a result of the 26.19 changes" |
| 10 | 26.19 nerfs: Nasus, Nocturne (R 160/130/100), Poppy, Rumble, Ryze, Vi (shield 12→10%) | correct | 26.19 notes: Nocturne R 140/115/90 ⇒ 160/130/100; Vi shield 12% ⇒ 10% |
| 11 | Master Yi Q refund is now a flat 1s | correct | 26.19 notes: "-1 second, scaling down with Ability Haste ⇒ 1 second" |
| 12 | World Atlas and Runic Compass trade health for health regen | correct | 26.19 notes |
| 13 | Top quest Teleport 420→390s; Unleashed Teleport 300–210s | correct | 26.19 notes: 420 ⇒ 390; Unleashed 330–240 ⇒ 300–210 |
| 14 | Team Voice for NA/OCE in 26.20 postponed, no new date | correct | 26.19 notes: "made the call to postpone this" |
| 15 | Phroxzon preview Sep 29–30; he called it the "final Worlds patch" | correct | [X post](https://x.com/RiotPhroxzon/status/2104800631001415990), read through the api.fxtwitter.com mirror, posted 2026-09-29 05:09 UTC: "This is the final World's patch". [Full preview](https://x.com/RiotPhroxzon/status/2105190591034462617) posted Sep 30 06:58 UTC |
| 16 | Preview nerfs Ambessa, Cassiopeia, K'Sante ("stale in pro play") | correct | Phroxzon, under "Stale Pro Champs": "Ambessa, Cassio, K'Sante have been stale for a while". Same nerfs in the final notes |
| 17 | Preview: Ashe AD growth 3.5→3 | correct | [GameRiv](https://gameriv.com/lol-patch-26-20-preview-all-buffs-nerfs-and-more/). Unchanged in the final notes |
| 18 | Preview: Yunara nerf aimed at level-1 laning | correct | GameRiv and outlets: Q on-hit 5–25 ⇒ 3–23, "oppressive level 1 laning". Final notes keep the same Q values and add "W slows no longer stack", which [Fanstanza](https://fanstanza.gg/lol-patch-26-20-notes-champion-buffs-nerfs/) already listed on Oct 1 |
| 19 | Preview item nerfs: Hexplate for ranged users, Runaan's bolt 65→60% AD, Rocketbelt (ability haste 20→10, bigger active) | correct | GameRiv: Hexplate ranged 70% ⇒ 50%; Runaan's 65% ⇒ 60%; Rocketbelt AH 20 ⇒ 10, active 100 (+10% AP) ⇒ 135 (+15% AP). Identical in the final notes |
| 20 | Preview buffs: Lucian, Vayne (flat 30-mana Q), Diana, Lillia (2.5/2.75/3s), Kennen, Mordekaiser, Neeko, Smolder, Swain, Tahm Kench | correct | GameRiv. Identical in the final notes (e.g. Vayne Q 46–30 ⇒ 30; Lucian AD/level 2.5 ⇒ 2.9) |
| 21 | Kindred: outlets disagree whether it's a buff or a nerf | unverifiable · **superseded** | Every outlet checked calls it a buff: GameRiv, [altchar](https://www.altchar.com/game-news/league-of-legends-patch-26.20-preview-champion-buffs-nerfs-items-changes-and-more-ax0un5s0FeOG), Fanstanza, [Hotspawn](https://www.hotspawn.com/league-of-legends/news/league-of-legends-patch-26-20), [Sportsdunia](https://www.sportsdunia.com/gaming/league-of-legends-patch-26-20-preview), [esportnow](https://esportnow.gg/lol/news/league-of-legends-patch-26-20-last-update-before-worlds-2026). None calls it a nerf. Final notes: "we're giving them buffs" |
| 22 | Varus and Sylas changes pulled; some outlets still list them | correct | GameRiv, Fanstanza and esportnow say both were pulled. altchar (Sep 29) still lists Varus and Sylas changes. The final notes mention neither |
| 23 | S1 "For Demacia" from 26.1 (Jan 8): map reskin and Demacia Rising PvE | correct | [Wiki 2026 annual cycle](https://wiki.leagueoflegends.com/en-us/Patch/2026_Annual_Cycle) ("Demacia-themed map"); 26.1 notes (Demacia Rising) |
| 24 | S2 "Pandemonium" from 26.9 (Apr 29), 6 patches | correct | Wiki annual cycle covers 26.9–26.14; 26.9 notes give the Apr 29 start |
| 25 | S3 "Classic" from 26.15 (Jul 29) to Jan 5, 2027; Act II "Riot Records" starts Oct 7 | mis-cited | True per the [wiki "Classic (Season 2026)" page](https://wiki.leagueoflegends.com/en-us/Classic_(Season_2026)): Act II "Riot Records" runs Oct 7–Jan 5, 2027. The cited annual-cycle page has no end date or Acts |
| 26 | Ranks reset only once a year, in January | mis-cited | True per [Hotspawn](https://www.hotspawn.com/league-of-legends/guide/lol-season-guide). Not in the cited wiki page or the [apex /dev](https://www.leagueoflegends.com/en-us/news/dev/dev-apex-tier-ranked-reset/), which describes only the Master+ mid-year reset |
| 27 | Master+ hard-reset at 26.9 in NA, EUW, EUNE, BR, LAN, TR | correct | [Apex /dev](https://www.leagueoflegends.com/en-us/news/dev/dev-apex-tier-ranked-reset/): reset to Master 0 LP in those six regions |
| 28 | 26.1 removed Feats of Strength, Atakhan and Blood Roses | correct | [26.1 notes](https://www.leagueoflegends.com/en-us/news/game-updates/patch-26-1-notes/) |
| 29 | Baron spawns at 20:00 again and scales with champion level | correct | 26.1 notes; [wiki Baron](https://wiki.leagueoflegends.com/en-us/Baron_Nashor): "reduced to 20:00 from 25:00", stats by level |
| 30 | First Blood +100g; first turret 300g shared among nearby allies | correct | 26.1 notes: "Nearby players are now rewarded a share of 300g" |
| 31 | Voidgrubs spawn once at 8:00 and despawn 14:45; Herald 15:00–19:45 | mis-cited | True per wiki [Voidgrub](https://wiki.leagueoflegends.com/en-us/Voidgrub) and [Rift Herald](https://wiki.leagueoflegends.com/en-us/Rift_Herald). Neither the 26.1 notes nor the cited Baron page gives these timings |
| 32 | Drakes first at 5:00, 75g each (was 25), stronger Vengeance; epic monsters scale with level | correct | 26.1 notes; [wiki Dragon pit](https://wiki.leagueoflegends.com/en-us/Dragon_pit) (5:00) |
| 33 | Plates permanent on outer, inner and inhibitor turrets; −10g/min from 11:00, capped at −40 | correct | 26.1 notes |
| 34 | Melee champions +20% damage to turrets | correct | 26.1 notes |
| 35 | Crystalline Overgrowth: next hit on a turret deals bonus damage | correct | 26.1 notes: after a 90s build-up, "the turret will take true damage the next time an enemy champion attacks it" |
| 36 | Nexus turrets respawn at 40% health | correct | 26.1 notes |
| 37 | Minions 0:30 (was 1:05), camps 0:55, Scuttle 2:55 | correct | 26.1 notes |
| 38 | Base crit damage 200% (was 175%) | correct | 26.1 notes |
| 39 | Lane-swap detection deleted | correct | 26.1 notes: "no more LANE SWAP DETECTED pop ups" |
| 40 | Role quests for every role, tied to the champion-select position (locks lanes) | correct | [Role Quest wiki](https://wiki.leagueoflegends.com/en-us/Role_Quest): quest follows the assigned role and changes "by swapping roles in champion select" |
| 41 | "each player's lane is visible in champion select" is why lanes lock | unverifiable | No source found saying positions are shown to the enemy, or giving this as the mechanism |
| 42 | Top (1,200): free Teleport, later Unleashed Teleport; level cap 20; bonus XP | correct | Role Quest wiki; 26.19 notes |
| 43 | Mid (1,350): free tier-3 boots; +6% AD/AP since 26.9, 8% since 26.11; replaced fast recall | correct | 26.9 notes; [26.11 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-11-notes/) (6% ⇒ 8%); Role Quest wiki |
| 44 | Bot (1,350): +300g, extra gold per minion and takedown, boots to quest slot | correct | 26.1 notes; Role Quest wiki |
| 45 | Jungle: pet treats, then gold, XP and movement speed | correct | Role Quest wiki |
| 46 | Support (800): World Atlas chain, 9g per 10s, control wards in quest slot, Vigilant Wardstone gone | correct | 26.1 notes: Wardstone "rolled into the support role quest" |
| 47 | Supports lose 33% away from bot lane until level 5 (26.16) | correct (wording) | [26.16 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-16-notes/): minion XP/gold penalty −25% until level 3 ⇒ −33% until level 5. The penalty is to XP and gold, not "points" |
| 48 | Faelights: +25% ward vision radius, 45s bonus reveal; 26.3 nerfed river reveals | correct | 26.1 notes; [26.3 notes](https://www.leagueoflegends.com/en-us/news/game-updates/patch-26-3-notes/) (river reveal now stops short of the scuttle pad and pit entrance) |
| 49 | 26.1 new items (Dusk and Dawn … Hexoptics C44 … Whispering Circlet → Diadem of Songs) | correct | 26.1 notes list all ten |
| 50 | The December preview used placeholder item names | unverifiable | No source found. [GameGrin](https://www.gamegrin.com/news/league-of-legends-2026-season-1-act-1-for-demacia-all-new-items-with-their-real-names/) (Dec 5, 2025) gives no placeholder-to-final name mapping |
| 51 | 26.1: Gunblade and Stormrazor return; Aegis of the Legion and Symbiotic Soles removed; Unending Despair armor-only | correct | 26.1 notes: Unending Despair MR 25 ⇒ 0, armor 25 ⇒ 50 |
| 52 | 26.9 items: Doran's Bow, Doran's Helm, Gluttonous Greaves new; Statikk and Voltaic reworked; Opportunity and Trailblazer removed | correct | [26.9 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-9-notes/) |
| 53 | 26.9 runes: Phase Rush removed; Deathfire Touch and Stormraider's Surge return; Arcane Comet reworked | correct | 26.9 notes |
| 54 | Sundered Sky nerfed repeatedly (26.16–26.17) | mis-cited | True: 26.16 cut its healing; [26.17](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-17-notes/) cut HP 450 ⇒ 400 and AD 45 ⇒ 40. The cited 26.1 and 26.9 notes came out before these patches |
| 55 | Autofilled players matched against each other by position; Aegis of Valor | mis-cited | True per [/dev: Ranked 2026](https://www.leagueoflegends.com/en-us/news/dev/dev-ranked-2026/) and the 26.1 notes. Not in the cited 26.15 notes or apex /dev |
| 56 | Since 26.15, Aegis means double LP on wins only, no loss protection | correct | [26.15 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-15-notes/): "will no longer reduce LP losses … wins will award double LP" |
| 57 | Climb indicator; full LP refunds for AFK/troll victims; early end when griefing is detected | mis-cited | True: Climb Indicator in /dev: Ranked 2026; [AFK refunds](https://bo3.gg/lol/news/riot-introduces-full-lp-refunds-for-matches-with-afk-players); [vote to end griefed games added in 26.10](https://u.gg/lol/news/patch-26-10-lets-league-of-legends-players-end-ruined-games-early). None of this is in the cited sources |
| 58 | Master+ dodge counts as a loss; bans apply to all of a person's accounts | mis-cited | True: /dev: Ranked 2026 ("a dodge will count as a full loss"); [Account Penalties FAQ](https://www.leagueoflegends.com/en-us/news/dev/account-penalties-and-enforcement-faq/) (penalty linking since Nov 19, 2025). Not in the cited sources |
| 59 | Since 26.15, Master duos limited to close ranks; GM and Challenger cannot duo | correct | 26.15 notes |
| 60 | WASD allowed in Ranked from around 26.9 | mis-cited | True per the 26.9 notes ("Enabled shortly after patch 26.9 goes live, including Clash"). Not in the cited 26.15 notes or apex /dev |
| 61 | League Classic (26.15): 60 champions on classic kits, with runes and masteries | correct | 26.15 notes: "60 champions using classic versions of their gameplay" |
| 62 | League Classic is unranked and 2013-era, uses IP, and grows through "Council" votes | mis-cited | True per [/dev: League of Legends Classic](https://www.leagueoflegends.com/en-us/news/dev/dev-league-of-legends-classic/): Season 3 as anchor, IP "back for Classic", The Council, draft/co-op/customs only. Not in the cited 26.15 notes |
| 63 | Swiftplay overhauled in 26.1 | mis-cited | True per the 26.1 notes. Not in the cited 26.15 notes |
| 64 | ARAM: Mayhem continues | correct | ARAM: Mayhem sections in the 26.15 and 26.20 notes |
| 65 | 173 champions | correct | Counted 173 in the [16.19.1 champion.json](https://ddragon.leagueoflegends.com/cdn/16.19.1/data/en_US/champion.json) |
| 66 | 2026 has exactly one new champion, Locke | correct | [esports.net](https://www.esports.net/news/lol/riot-games-confirms-only-one-new-champion-for-2026-amid-league-next-development/) (Meddler) |
| 67 | Locke: Demacian AP assassin, mid lane, released 26.13 on Jun 24 | correct | [26.13 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-13-notes/) ("June 24th"); Data Dragon tags Assassin/Mage, blurb "progeny of Demacian occultists" |
| 68 | Most of the champion team moved to League Next | correct | esports.net: "most of the team focused on League Next" |
| 69 | League Next is a 2027 overhaul: new client, Rift visual update, rune and pre-game changes | mis-cited | True per [Dexerto](https://www.dexerto.com/league-of-legends/riot-confirms-plans-for-lol-shakeup-in-2027-with-new-visuals-client-3296182/). The cited esports.net article doesn't describe these |
| 70 | Yunara released Jul 16, 2025; Zaahen Nov 19, 2025 | mis-cited | True per the wiki ([Yunara](https://wiki.leagueoflegends.com/en-us/Yunara) V25.14, [Zaahen](https://wiki.leagueoflegends.com/en-us/Zaahen) V25.23). The cited Data Dragon, esports.net and 26.13 sources have no release dates |
| 71 | 2026 updates: Mel (26.3), Shyvana (26.6), Zeri (26.9), Bel'Veth (26.15) | mis-cited | True per the [26.3](https://www.leagueoflegends.com/en-us/news/game-updates/patch-26-3-notes/), [26.6](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-6-notes/), 26.9 and 26.15 notes. The cited sources cover only Shyvana |
| 72 | Top meta: Yone, Malphite, Aatrox, Garen, Darius most picked; Malphite 51.5% / 16.6% ban; Jayce and K'Sante 47–48% | correct | [op.gg top](https://op.gg/lol/champions?position=top): pick 8.5/7.1/6.4/6.4/6.3%; Malphite 51.49% / 16.52% ban; Jayce 47.69%, K'Sante 47.18% |
| 73 | Jungle: Lee Sin 12.9% pick, slightly below average; Wukong, Rammus, Cho'Gath, Warwick, Lillia strong | correct | [lolalytics](https://lolalytics.com/lol/tierlist/): Lee Sin 12.91% pick, 50.80% vs 51.72% average; op.gg Wukong 52.18%, Rammus 52.33% |
| 74 | Mid: Viktor, Ahri, Yasuo most picked; Vex, Ekko, Fizz, TF, Xerath strong; Orianna, Ryze, Mel about 45–46% | correct | [op.gg mid](https://op.gg/lol/champions?position=mid): Vex 52.10%, Ekko 51.50%; Orianna 46.30%, Ryze 45.40%, Mel 45.38% |
| 75 | Bot: Jinx 17% / about 52.4%; Yunara 16% (from 4.7% on 26.12); Ezreal about 11% / 45.8% | correct | [op.gg ADC](https://op.gg/lol/champions?position=adc): Jinx 17.05% / 52.47%, Yunara 16.01%, Ezreal 11.24% / 45.70%. [lolalytics 16.12](https://lolalytics.com/lol/yunara/build/?patch=16.12): Yunara 4.65% |
| 76 | Support: Thresh 15% strong; Braum, Leona, Blitz strong; Mel and Karma weak | correct | [op.gg support](https://op.gg/lol/champions?position=support): Thresh 15.02% / 51.98%; Mel 41.92%, Karma 48.67% |
| 77 | Bans: Locke about 30% (34% M+), Nasus 25%, Pyke 35.7% M+, Yasuo, Caitlyn | correct | op.gg: Locke 30.18% / [34.32% M+](https://op.gg/lol/champions?position=mid&tier=master_plus); Nasus 24.93%. [lolalytics](https://lolalytics.com/lol/pyke/build/?tier=master_plus): Pyke M+ 35.72% |
| 78 | Lethal Tempo near-universal (Jinx, Yunara 98%); Jhin Fleet; Jinx Hexoptics → Runaan's → IE | correct | [op.gg Jinx](https://op.gg/lol/champions/jinx/build/adc): LT 98.2%, that core order. [Yunara](https://op.gg/lol/champions/yunara/runes/adc): LT pages total about 98.1%. Jhin: Fleet |
| 79 | Deathfire Touch dominates mages (Viktor 93%) | correct | [op.gg Viktor runes](https://op.gg/lol/champions/viktor/runes/mid): DFT pages 69.27 + 21.32 + 1.73 ≈ 92.3% |
| 80 | Conqueror for Lee Sin and Aatrox; Electrocute for Ahri, Aurora and Locke; Locke Lich Bane → Shadowflame → Zhonya's | correct | op.gg build pages for each champion |
| 81 | Engage supports: Aftershock, Locket → Knight's Vow → Bandlepipes | correct | [op.gg Leona](https://op.gg/lol/champions/leona/build/support) |
| 82 | Late-2026 playoffs dataset: patches 26.16–26.17, 178 games across LCK, LPL, LEC, LCS | correct | gol.gg event totals: LCK playoffs 41 + LPL Grand Finals 55 + LPL Regional Finals 12 + LEC Summer playoffs 31 + LCS Summer playoffs 39 = 178, all on 16.16/16.17. The cited link covers only the LCK |
| 83 | Cassiopeia 93% presence, 160 bans in 178 games | correct | Aggregated from gol.gg champion tables: 6 picks + 160 bans = 166/178 = 93.3%. The LCK page alone shows 88% |
| 84 | Jungle: Nocturne 82%, Vi 74%, then J4, Lee Sin, Naafiri, Qiyana | correct | Same aggregation: Nocturne 81.5%, Vi 74.2%, J4 47.2%, Lee 40.4%, Naafiri 30.9%, Qiyana 28.7% |
| 85 | Top, mid, bot and support pro priorities; Azir, Taliyah, Aurora, Rell, Neeko faded | correct | Aggregate presence: Olaf 57%, Rumble 40%, Orianna 54%, Akali 44%, Ezreal 42%, Lulu 36%, Seraphine 35%; Azir 6%, Taliyah 10%, Aurora 7%, Rell 8%, Neeko 11%. Engage supports Nautilus (32%) and Bard (30%) are also high |
| 86 | At MSI and EWC, bot lanes were often mages or non-ADCs (Ziggs, Mel, Syndra, Seraphine) | correct | gol.gg, bot role only: MSI Ziggs 15 and Mel 10 of 142 bot picks; EWC Ziggs 15, Syndra 4, Seraphine 4 of 102 |
| 87 | 26.18 nerfed Cassiopeia, Syndra, Seraphine, Nautilus, Bard; 26.19 nerfed Nocturne, Vi, Ryze, Rumble, Poppy | correct | [26.18 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-18-notes/) (the notes use the phrase "pro skew"); 26.19 notes |
| 88 | Fearless continues; First Selection (side *or* draft order) everywhere | correct | [lolesports season start](https://lolesports.com/en-US/news/season-start-2026-lol-esports): "First Selection will roll out in all regions" |
| 89 | LCK Cup: Gen.G 3–0 BNK FearX, in Hong Kong | correct | gol.gg (Mar 1); [Wikipedia 2026 LCK](https://en.wikipedia.org/wiki/2026_LCK_season) (Kai Tak Sports Park) |
| 90 | First Stand (São Paulo): BLG 3–1 G2; G2 3–0 Gen.G in the semifinal | correct | gol.gg (Mar 21–22); São Paulo per the lolesports season-start post |
| 91 | MSI (Daejeon): HLE 3–2 BLG; Zeus Finals MVP; LYON beat G2 and finished 3rd | correct | [gol.gg MSI](https://gol.gg/tournament/tournament-matchlist/MSI%202026/): LYON 3–0 G2, then 2–3 HLE in the lower final; [LCK on X](https://x.com/LCK/status/2076302228638568855) (Zeus MVP) |
| 92 | EWC: DK 3–0 KC; event moved from Riyadh to Paris | correct | gol.gg (Jul 19). Move confirmed by [Deadline](https://deadline.com/2026/05/2026-esports-world-cup-move-paris-riyadh-iran-war-1236917595/) (security concerns from the Iran war), so the "(unverified)" caveat can go |
| 93 | LCK: Gen.G 3–1 HLE in the final; Chovy season MVP | correct | gol.gg (Sep 13); Wikipedia 2026 LCK |
| 94 | LPL: BLG won Splits 1 and 2; AL 3–1 BLG in the Grand Finals; FPX and RNG left | correct | gol.gg (BLG 3–1 JDG, BLG 3–0 TES, AL 3–1 BLG); [Wikipedia 2026 LPL](https://en.wikipedia.org/wiki/2026_LPL_season) |
| 95 | LEC: G2 won all three splits | correct | gol.gg: G2 3–2 KC, 3–2 KC, 3–0 MKOI |
| 96 | LCS back after the LTA was scrapped; TL 3–1 LYON (Oct 4) | correct | gol.gg (Oct 4, patch 16.17); [GosuGamers](https://www.gosugamers.net/lol/news/77398-riot-games-announce-lcs-and-cblol-will-return-in-2026) |
| 97 | LCP: TSW won all three splits | correct | gol.gg: TSW 3–0 DCG, 3–1 DCG, 3–0 CFO |
| 98 | Asian Games: Korea won gold | correct | [Inven Global](https://www.invenglobal.com/articles/26768/south-korea-finishes-asian-games-esports-with-2-gold-1-silver-2-bronze) (3–0 Chinese Taipei, Oct 2) |
| 99 | Caps is the first Western Hall of Legends inductee | correct | [esports.gg](https://esports.gg/guides/league-of-legends/hall-of-legends-caps-bundles-whats-inside/) |
| 100 | Worlds dates: Play-In Oct 15–18, Swiss Oct 23–31, QF/SF Nov 3–8, Final Nov 14 | correct | [Worlds primer](https://lolesports.com/en-US/news/worlds-2026-primer) |
| 101 | Venues: Riot Games Arena (LA), Allen TX for Swiss through semifinals, Barclays Center for the final | mis-cited | True per Riot's [MSI and Worlds Updates](https://lolesports.com/en-US/news/msi-and-worlds-updates) and [Wikipedia](https://en.wikipedia.org/wiki/2026_League_of_Legends_World_Championship). The primer names cities only ("Knockout Stage – Allen, TX, and Brooklyn, NY") |
| 102 | 19 teams; LCK and LPL 4 seeds each; Swiss Bo1/Bo3; knockouts Bo5 | correct | Primer: 4+4+3+3+3+2 teams; "Swiss Stage (Bo1, Bo3)"; "Knockout Stage (Bo5)" |
| 103 | No games played as of Oct 6 | correct | Primer: Play-In starts Oct 15 |
| 104 | "The draw is Oct 10" (also in Unknown) | **WRONG** | Primer: Oct 10 is only the **Play-In** draw. The Swiss Round 1 draw is **Oct 18** and the quarterfinal draw Oct 31 |
| 105 | Seeds by region; KT (2025 finalist) did not qualify | correct | Primer team list; [Dexerto](https://www.dexerto.com/league-of-legends-esports/t1-beat-kt-rolster-to-claim-third-straight-league-of-legends-world-championship-3281079/) (2025 final T1 3–2 KT) |
| 106 | CBLOL 1st seed is LOS or FURIA, decided Oct 10 | correct | Primer (CBLOL Finals Oct 10); gol.gg (LOS and FURIA won the bracket finals) |
| 107 | Play-In: KC, C9, MVK and the CBLOL 2nd seed; Bo5 double elimination; one advances | correct | Primer |
| 108 | T1: Doran/Oner/Faker/Peyz/Keria; Gumayusi now at HLE | correct | [gol.gg game 82745](https://gol.gg/game/stats/82745/page-game/) |
| 109 | Faker signed through 2029 | mis-cited | True per [Sheep Esports](https://www.sheepesports.com/en/articles/lol-faker-extends-with-t1-until-2029/en). Not on the cited gol.gg game page |
| 110 | HLE, Gen.G, BLG and G2 rosters | correct | gol.gg games 82745, 82962, 82967, 83082 match exactly |
| 111 | Expert: how 2026 plays (factual parts: no Atakhan or Feats, decaying plates, melee bonus, 0:30 wave, Baron 20:00, swap and roam penalties) | correct | 26.1 and 26.16 notes; the interpretation itself was not scored |
| 112 | Top's quest Teleport frees top laners from taking Teleport; Riot says top "loses influence at higher tiers" | correct (wording) | 26.19 notes: "Role quest free Teleport". The quote is not verbatim. [Phroxzon](https://x.com/RiotPhroxzon/status/2100090657494987053) wrote: "Top Lane is underpowered at those higher skill brackets" |
| 113 | Cassiopeia, K'Sante, Orianna, Ryze are pro priorities but under 50% in solo queue | correct | op.gg: 48.4 / 47.2 / 46.3 / 45.4%; gol.gg presence 93 / 32 / 54 / 37% |
| 114 | Riot nerfs "pro skew" picks and protects solo queue; 26.18–26.20 tuned around Worlds | correct | 26.18 notes ("pro skew"); Phroxzon calls SoloQ "a high priority" |
| 115 | KR Master+: Lee Sin 56% ban; Yunara, Jayce, Viktor high | correct | [op.gg KR M+](https://op.gg/lol/champions?position=jungle&region=kr&tier=master_plus): Lee Sin 56.18% ban; Yunara top ADC pick at 25.96%; Jayce 26.33% ban |
| 116 | lolalytics Emerald+ average about 51.7%; Jinx 54.4% there vs 52.5% on op.gg | correct | lolalytics "Average Emerald+ Win Rate: 51.72%", Jinx 54.41%; op.gg Jinx 52.47% |
| 117 | Yunara's rise followed the 26.16 Runaan's buff, which 26.20 partly reverts | correct | 26.16: 55% ⇒ 65%; 26.20: 65% ⇒ 60%. lolalytics Yunara pick: 5.38% (16.15), 6.91% (16.16), 9.14% (16.17), 15.97% (16.19) |
| 118 | Phroxzon = Matt Leung-Harrison, Lead Gameplay Designer (champions, balance, preseason, modes); previews about 8 days before a patch | correct | [His X announcement](https://x.com/RiotPhroxzon/status/1707117865692995807). 26.20 preview Sep 29 for Oct 7; 26.19 preview Sep 16 for Sep 23 |
| 119 | Notes land about 18:00 UTC the day before the patch | correct | 26.19: 2026-09-22T18:00Z; 26.20 on Oct 6. Winter patches post at 19:00Z (e.g. 26.1) |
| 120 | Dev Update videos come with written TL;DW recaps | correct | [TL;DW: Team Voice, Classic & More](https://www.leagueoflegends.com/en-us/news/dev/tldw-team-voice-classic-more-dev-update/) |
| 121 | Balance framework (Average/Skilled/Elite/Pro) dates from 2020; no 2026 update | correct (wording) | [/dev: Balance Framework Update](https://www.leagueoflegends.com/en-us/news/dev/dev-balance-framework-update/) (Jun 30, 2020). It was first introduced in 2019; no later update found |
| 122 | Pro play about one patch behind; Worlds starts on 26.20; 26.21 lands mid-event | correct | gol.gg patch column (16.16–16.17); schedule (26.21 on Oct 21) |
| 123 | Role quests as "homework" (Hupu) vs Riot's "rock-paper-scissors" pitch; /dev framed 2026 as strategy-first to Korean players | unverifiable | No source found for any of these |
| 124 | Kanavi: "Jungle is definitely pretty bad" | correct | [Inven Global](https://www.invenglobal.com/articles/20054/lck-players-react-to-2026-preseason-patch-teleport-still-essential-for-top-lane-jungle-rewards-underwhelming) |
| 125 | Korean press calls non-ADC bot "the keyword of 2026" | correct (wording) | [Gameple](https://www.gameple.co.kr/news/articleView.html?idxno=216083): "one of the keywords" of the 2026 international events |
| 126 | Season 2 pass cut skin choices and was walked back | unverifiable | The cut is confirmed: [Fiendish orbs replaced skins](https://esports.gg/news/league-of-legends/skins-available-lol-fiendish-mystery-orbs/). No walk-back found, and [turbosmurfs](https://turbosmurfs.gg/article/all-lol-battle-pass) says the change carried into S3 |
| 127 | Brazilian court fined Riot R$15M over loot boxes; not final | correct | [white.market](https://news.white.market/latest/brazil-court-fines-riot-r15m-in-r298m-league-loot-box-case/): ruling of June 9; appeal period reopened |
| 128 | Caps' Hall of Legends bundle costs 58,865 RP | correct | esports.gg: Signature Collection 58,865 RP |
| 129 | LTA failed; LCS returned with 8 teams; LPL shrank from 16 to 14 | correct | [Wikipedia 2026 LCS](https://en.wikipedia.org/wiki/2026_LCS_season) (8 teams); [Esports Advocate](https://esportsadvocate.net/2026/01/lpl-set-to-shrink-to-14-teams-for-2026/) |
| 130 | Vanguard On-Demand needs Win11 25H2, Secure Boot, TPM and VBS; about 35% eligible | correct | [GosuGamers](https://www.gosugamers.net/news/78679-riot-games-vanguard-on-demand-lets-lol-valorant-and-2xko-players-run-anti-cheat-on-demand) |
| 131 | 296k accounts actioned for rank manipulation (2026-09) | correct (wording) | [Techtroduce](https://www.techtroduce.com/riot-296416-league-valorant-rank-manipulation): 296,416, Riot update of Sep 17, 2026. The figure is LoL and VALORANT combined |
| 132 | "Under 1% of games have a scripter" dates from 2024 | correct | [/dev: Vanguard x LoL Retrospective](https://www.leagueoflegends.com/en-us/news/dev/dev-vanguard-x-lol-retrospective/) (Aug 22, 2024) |

## Wrong claims and corrections

1. **Mid-patch updates** (line 22: "only 26.1, 26.3, 26.6 and 26.9 had one in 2026"). **Correction:** 26.10 had one too. Riot micropatched a Smolder nerf one day into 26.10. Phroxzon posted "We just pushed a micropatch nerf to Smolder" (2026-05-15 00:17 UTC), and the [26.10 notes](https://www.leagueoflegends.com/en-us/news/game-updates/league-of-legends-patch-26-10-notes/) carry it as an undated inline "Update:" in the Smolder section: base AD 60 ⇒ 58, plus Q, W and R damage cuts. The four dated sections are real: 26.1 (Jan 9), 26.3 (Feb 5), 26.6 (Mar 20), 26.9 (Apr 30). No mid-patch updates were found in 26.2, 26.4, 26.5, 26.7, 26.8 or 26.11–26.19. Suggested text: "only 26.1, 26.3, 26.6 and 26.9 (dated sections) and 26.10 (an undated Smolder 'Update') had one."
2. **Worlds draw date** (line 145, "The draw is Oct 10"; repeated in Unknown, line 193, "Worlds 2026 draw … decided on Oct 10"). **Correction:** Oct 10, after the CBLOL Finals, is only the **Play-In** draw. The **Swiss Stage Round 1 draw is Oct 18**, after the Play-In. Later Swiss rounds are drawn Oct 23, 24, 26 and 30, and the quarterfinal draw is Oct 31 ([primer](https://lolesports.com/en-US/news/worlds-2026-primer)). Only the CBLOL 1st seed is decided on Oct 10.

## Superseded by the final 26.20 notes

- The final notes changed **none of the preview numbers** the briefing quotes. Unchanged: Ashe AD/level 3.5 ⇒ 3, Lillia R 2.5/2.75/3s, Vayne Q 30 mana, Lucian AD/level 2.5 ⇒ 2.9, Yunara Q on-hit 5–25 ⇒ 3–23, Hexplate ranged 70% ⇒ 50%, Runaan's 65% ⇒ 60%, Rocketbelt AH 20 ⇒ 10 with active 135 (+15% AP). Varus and Sylas are absent.
- **Row 5 and Unknown line 192:** "notes not yet published" and "26.20 final numbers" are now out of date.
- **Row 21 (Kindred):** the final notes call the changes buffs: "we're giving them buffs" (W monster mod 150% ⇒ 165%, E slow 1s ⇒ 1.5s, E no longer targets small monsters).
- Also in the final notes but not in the briefing: Yunara's W slows no longer stack with other slows. Preview coverage already listed this as a bugfix by Oct 1.

## Wording fixes (claims are true, counted as correct)

- Row 47: the 26.16 support penalty reduces **minion XP and gold**, not "points".
- Row 112: "loses influence at higher tiers" is not a Riot quote.
- Row 125: Gameple wrote "one of the keywords", not "the keyword".
- Row 131: the 296,416 figure covers LoL **and** VALORANT.
- Row 121: the balance framework dates from 2019; its public update is from 2020.
- Unknown line 195: why EWC moved to Paris can now be answered. Deadline and Dexerto report security concerns linked to the Iran war.

# Agent 2 notes: high-MMR European pub meta (position 3, 7000+ MMR)
Written 2026-10-07 (UTC ~15:30-). All stats "as of 2026-10-07" unless a window is given.

## Access log
- Dotabuff (https://www.dotabuff.com/heroes/lanes?lane=off&date=7d&rankTier=immortal) -> HTTP 403 via WebFetch, tried once, not retried.
- Stratz (https://stratz.com/heroes?positionIds=2&rankBracket=8&regionIds=2) -> HTTP 403 via WebFetch, tried once, not retried.
- OpenDota REST + explorer work (curl through proxy). Explorer has a ~15 s "Query read timeout"; keep windows to <= ~1-2 h for public_matches scans or aggregate client-side.

## Patch window (primary: dota2.com datafeed)
- https://www.dota2.com/datafeed/patchnoteslist?language=english (fetched 2026-10-07): last entries 7.41 = 2026-03-24T07:00Z, 7.41a 2026-03-27, 7.41b 2026-04-07, 7.41c 2026-05-06, 7.41d 2026-06-04, 7.41e 2026-07-30, 7.41f = 2026-09-15T07:00Z (unix 1789455600). 7.41f is the LAST entry in the list as of 2026-10-07 => current patch = 7.41f (confirms the unverified belief). Caveat: datafeed times are 07:00Z (= 00:00 PDT) round numbers; OpenDota's own patch table puts 7.41 at 2026-03-24T00:50Z, i.e. the datafeed stamp can be hours later than the real roll-out. OpenDota's patch list (https://api.opendota.com/api/constants/patch) only knows numbered patches (latest "7.41", id 60) -> its `match_patch`/patch id cannot isolate 7.41f; must filter by start_time.
- My "7.41f window" = start_time >= 1789455600 (2026-09-15 07:00Z) to 2026-10-07 (~22 days).

## OpenDota data limits found (important for method)
- Explorer `matches`/`player_matches` hold only league/pro matches recently (60 days to 2026-10-07: 1,315 rows, all lobby_type 1). Public pub matches live only in `public_matches` (no per-player rows, no lane_role, no positions). `parsed_matches` -> "permission denied". So position-3 filtering of pubs is NOT possible from the explorer.
- `public_matches` columns: match_id, match_seq_num, radiant_win, start_time, duration, lobby_type, game_mode, avg_rank_tier, num_rank_tier, cluster, radiant_team[], dire_team[] (hero ids in player_slot order 0-4 / 128-132; verified against /api/matches/{id}).
- Volume: ~27k public matches per hour, ~490k ranked (lobby_type 7) matches per day (2026-10-01).
- avg_rank_tier is an INTEGER and its max is 75 (no 76-79, no 80+). Checked 2026-09-16 07:00-09:00Z: floor values 71-75, 61-65, ...; `avg_rank_tier >= 80` returns 0 rows. In sample matches in the 75 bucket (match 9033300054, 9033300730) players were mostly rank_tier 80 (Immortal) or 75 (Divine 5). So the top bucket "75" = Divine-5-or-Immortal average lobbies; OpenDota cannot separate 7000+ from Divine 5 by lobby average.
- /api/heroStats `8_pick`/`8_win` (Immortal bracket) are all 0 for every hero (checked 2026-10-07). Brackets 1-7 are populated (rolling 7 days; pub_pick sums to 41.27M picks = ~4.13M matches). So the top bracket OpenDota exposes is 7 (avg_rank_tier 70-79, "Divine").
- Cluster -> region (upstream https://raw.githubusercontent.com/odota/dotaconstants/master/build/cluster.json and region.json, fetched 2026-10-07; the API's /constants/cluster is older and lacks some ids): 131-138 and 271-274 = region 3 EUROPE; 189 = region 28 WARSAW; 191-193 = region 9 AUSTRIA; 181-188 = region 8 STOCKHOLM (= the Russia servers; peak 17-18 UTC); 381/382 = 15 PERU; 410, 412 = 2 US EAST. Clusters 413/414/415/417 and 436 are NOT in the constants (413-417 peak 13-14 UTC like SE Asia; 436 peaks 20 UTC, ~6.2k ranked matches/day, region unknown).
- Ranked (lobby_type 7) matches per cluster on 2026-10-01 (all ranks): 271 12,870; 272 14,406; 273 15,325; 274 12,039 (EU peak 18-20 UTC); 189 17,233 (Warsaw, peak 19 UTC); 191/192/193 ~3.3-3.8k each but only active ~15:00-21:00 UTC; Russia 181-187 ~9.8-30k each; 131-138: not in top 34 clusters that day.

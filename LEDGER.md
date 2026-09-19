# Ledger

One row per pass. Append only; never edit an earlier row. Agents fill the first seven cells; Daniel fills the last five. A blank Daniel cell older than 7 days reads as `ungraded`. The agent's seven cells arrive as the `ledger:` line at the end of the PR body, or of the thread's final message for `empty` and `needs-decision` passes; the two one-liners in `README.md` append them.

Columns: `#` pass number · `date` · `repo` · `request` (Daniel's `request=` line, or `inferred: …`) · `runtime` (`orb-high`, `local-high`, other) · `thread` (`T-…`) · `output` (PR URL, `report`, `empty`, `needs-decision`, `blocked`) · `grade` (`merged`, `merged-after-fix`, `closed-not-useful`, `closed-wrong-job`, `empty-right`, `empty-missed`, `ungraded`) · `fix` (`none`, `wrong-scope`, `wrong-fix`, `missing-decision`, `wrong-job`) · `daniel_min` (minutes to read, decide and correct) · `saved_min` (Daniel's estimate of the time the merged work saved; merged rows only) · `limitation` (at most 12 words, or `same as #N` when it repeats an earlier row's limitation; a `same as` cell is the only software trigger).

Correction burden per pass is `fix` plus `daniel_min`. Value is the count of merged rows and the sum of `saved_min` against the sum of `daniel_min`.

| # | date | repo | request | runtime | thread | output | grade | fix | daniel_min | saved_min | limitation |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | 2026-09-14 | Pain-Point-Pipeline/amp-fit-v2 | Find and repair current failing checks; deliver PRs (pre-amp-fit launch, see postmortem §4.3) | orb-high | T-01a0a078-4920-7151-b73f-e7df654347fe | https://github.com/Pain-Point-Pipeline/amp-fit-v2/pull/27 | merged | none | 8 | 10 | Failure existed only where accounts.json is absent; workbank area still non-hermetic |
| 2 | 2026-09-14 | Pain-Point-Pipeline/amp-fit-v2 | same launch as row 1 | orb-high | T-01a0a078-4920-7151-b73f-e7df654347fe | https://github.com/Pain-Point-Pipeline/amp-fit-v2/pull/28 | merged | none | 12 | 30 | Fixture hygiene on apparatus retired 2026-09-16; product path untouched |

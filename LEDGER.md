# Ledger

One row per pass, and only passes launched with the amp-fit skill get rows. Append only; never edit an earlier row. Agents fill the first seven cells; Daniel fills the last five. A blank grade older than 7 days reads as `ungraded`, which counts as not useful. The agent's seven cells arrive as the `ledger:` line at the end of the PR body, or of the thread's final message for `empty` and `needs-decision` passes; the one-liners in `README.md` append them. A thread that dies without a final message emits no `ledger:` line, so Daniel writes its row by hand with output `blocked`.

Columns: `#` pass number · `date` · `repo` · `request` (Daniel's `request=` line, or `inferred: …`) · `runtime` (`orb-high`, `local-high`, other) · `thread` (`T-…`) · `output` (PR URL, `empty`, `needs-decision`, `blocked`) · `grade` (by output, below) · `fix` (`none`, `wrong-scope`, `wrong-fix`, `missing-decision`, `needless-question`, `wrong-job`) · `daniel_min` (minutes to read, decide and correct) · `saved_min` (Daniel's estimate of the time the merged work saved; merged rows only) · `limitation` (at most 12 words, or `same as #N` when it repeats an earlier row's limitation; a `same as` cell is the only software trigger).

Grades by output. A PR: `merged`, `merged-after-fix`, `closed-not-useful`, or `closed-wrong-job`. `empty`: `empty-right`, or `empty-missed` when there was work to do, with fix `wrong-job`. `needs-decision`: `asked-right` when the decision was Daniel's and the work could not go on without it, or `asked-wrong` when Amp should have proceeded (fix `needless-question`) or asked about the wrong job (fix `wrong-job`). `blocked`: `void`, recorded but not judged.

Graded rows are rows with any grade except `void`; a `void` row counts as neither graded nor ungraded, though its minutes and limitation still count. Merged means `merged` or `merged-after-fix`. Correction burden per pass is `fix` plus `daniel_min`. Value is the count of merged rows and the sum of `saved_min` against the sum of `daniel_min`.

| # | date | repo | request | runtime | thread | output | grade | fix | daniel_min | saved_min | limitation |
|---|---|---|---|---|---|---|---|---|---|---|---|

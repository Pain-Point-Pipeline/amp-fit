# amp-fit

Finish the thing the owner of this repo keeps coming back to and has not finished, and return it as one pull request they can merge; anything else you notice goes in one line at the bottom of the PR, not in the diff.

That sentence is the product. The skill in `skills/amp-fit/` performs it. `LEDGER.md` is the proof. Nothing else gets built until a graded row says `same as #N` in its limitation cell. Why: [cases/2026-09-19-postmortem-v1-v4.md](cases/2026-09-19-postmortem-v1-v4.md). Audience for now: Daniel; the ledger and cases carry no secrets or private paths, so this repository can be made public later without editing.

## The loop

1. Daniel launches one pass with one line at the start of a working session in that repo; the line is the authorization, `n` is the next ledger row, and `request=` is optional. Once per machine and per repo: [SETUP.md](SETUP.md).
   - Orb, primary, with the message directly after `-ox` (a trailing message is rejected): `amp -ox "amp-fit pass. n=<row> repo=<owner/repo> request=<one line>" --mode high --project <owner/repo> --no-archive-after-execute --visibility private`
   - Local fallback, interactive so permission prompts can be answered: `cd <clone> && amp --mode high`, then type the same launch line.
2. Amp performs the pass and returns one PR on branch `amp-fit/<n>`, or a final message `empty` / `needs-decision`.
3. Daniel grades before the session ends, within 72 hours at most: read, merge or close, append the row, fill the last five cells (`grade`, `fix`, `daniel_min`, `saved_min`, `limitation`). A row ungraded after 7 days counts as not useful.
   - `gh pr view <PR-URL> --json body --jq .body | sed -n 's/^ledger: //p' >> LEDGER.md`
   - `amp threads markdown <T-id> | sed -n 's/^ledger: //p' >> LEDGER.md` for `empty` and `needs-decision` passes
4. After a first merge on a responsibility, Daniel may tell that thread to run on a schedule (Amp Automations). The next run reads what changed and never replays.

## Stop rules (edit the numbers here, nowhere else)

- At most one launch per day; at most two ungraded rows at any time.
- Two of any five consecutive rows `closed-wrong-job`: change only the job sentence above and in SKILL.md, citing the rows.
- Five graded rows on one repo with fewer than two merged: change the repo, not the skill.
- Three consecutive `empty-*` rows on Daniel-named repos: recruit one other real owner before changing anything.
- A graded row whose `limitation` reads `same as #N`: the only software trigger. One file, at most 200 lines, commit cites both rows.
- Fewer than 10 graded rows by 2026-10-10: the bottleneck is owner time; record that and stop rather than automate around it.
- 10 graded rows across two repos with under 40 % merged: stop the product, write one postmortem of at most 40 lines, no v6.
- SKILL.md over 80 lines, this file over 40, or SETUP.md over 15: revert. A pass whose diff is in this tree is not a pass and gets no row.

## Daniel's checklist

- [ ] Case zero: grade amp-fit-v2 PRs #27 and #28. Rows 1 and 2 are pre-filled; about 10 minutes, $0.
- [x] Smoke test passed for `iamdanielkitchen/food-bridge-app` (SETUP.md step 4); result recorded in the postmortem §16.
- [ ] Pass 1, decided 2026-09-19, launch line: `amp-fit pass. n=3 repo=iamdanielkitchen/food-bridge-app request=Do the surviving KEEPER first-audit items as one PR: remove yonder-app/_stage-harness.tmp.mjs if nothing references it, fix the stale detour-app paths in CLAUDE.md and README.md, banner superseded docs. Do not build KEEPER. Put the KEEPER-build and WP-9 spend decisions under What is unresolved.`
- [ ] Checkpoints: 2026-09-28 (at least one merged?) and 2026-10-03 (two merged on two repos means the next step is an outside owner, after five merges).

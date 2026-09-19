# amp-fit

Finish the thing the owner of this repo keeps coming back to and has not finished, and return it as one pull request they can merge; anything else you notice goes in one line at the bottom of the PR, not in the diff.

That sentence is the product. The skill in `skills/amp-fit/` performs it. `LEDGER.md` is the proof. Nothing else gets built until the same limitation text appears in two graded ledger rows. Why: [cases/2026-09-19-postmortem-v1-v4.md](cases/2026-09-19-postmortem-v1-v4.md).

## The loop

1. Daniel launches one pass with one line; the line is the authorization and `request=` is optional.
   - Orb, primary: `amp -ox --mode high --project <owner/repo> --no-archive-after-execute --visibility private "amp-fit pass. repo=<owner/repo> request=<one line>"`. Once per repo before that: `amp projects create <owner/repo> --personal --ship-behavior custom --custom-ship-prompt-file skills/amp-fit/ship.md --json`. Until an Orb pass shows the installed skill loads there, paste the body of `skills/amp-fit/SKILL.md` ahead of the launch line.
   - Local fallback, interactive so permission prompts can be answered: `cd <clone> && amp --mode high`, then type the same launch line.
2. Amp performs the pass and returns one PR on branch `amp-fit/<n>`, or a final message `empty` / `needs-decision`.
3. Daniel grades within 72 hours: read, merge or close, fill five cells of the row in `LEDGER.md` (`grade`, `fix`, `daniel_min`, `saved_min`, `limitation`). A row ungraded after 7 days counts as not useful.
4. After a first merge on a responsibility, Daniel may tell that thread to run on a schedule (Amp Automations). The next run reads what changed and never replays.

Install once: `amp skill add --global /home/danielkitchen/Documents/Repos/amp-fit/skills/amp-fit`.

## Stop rules (edit the numbers here, nowhere else)

- At most one launch per day; at most two ungraded rows at any time.
- Two of any five consecutive rows `closed-wrong-job`: change only the job sentence above and in SKILL.md, citing the rows.
- Five graded rows on one repo with fewer than two merged: change the repo, not the skill.
- Three consecutive `empty-*` rows on Daniel-named repos: recruit one other real owner before changing anything.
- Identical `limitation` text in two graded rows: the only software trigger. One file, at most 200 lines, commit cites both rows.
- Fewer than 10 graded rows by 2026-10-10: the bottleneck is owner time; record that and stop rather than automate around it.
- 10 graded rows across two repos with under 40 % merged: stop the product, write one postmortem of at most 40 lines, no v6.
- SKILL.md over 80 lines or this file over 40: revert. A pass whose diff is in this tree is not a pass and gets no row.

## Daniel's checklist

- [ ] Case zero: grade amp-fit-v2 PRs #27 and #28. Rows 1 and 2 are pre-filled; about 10 minutes, $0.
- [ ] First case, decided 2026-09-19: `iamdanielkitchen/food-bridge-app`. Create its personal Amp project or use the local fallback; give a `request=` line or leave the job to inference.
- [ ] Checkpoints: 2026-09-28 (at least one merged?) and 2026-10-03 (two merged on two repos means the next step is an outside owner, after five merges).

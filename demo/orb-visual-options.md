# Orb card — what this frame is, and the upgrades

Written 2026-09-21, from the screenshot of the live demo card and from the stored run that produced it. No demo behavior, skill text, or ledger row was changed.

## Answer

That frame is the resting picture after the pass has already finished. It is a faithful rendering of the last thing the skill requires the Orb to write. It is a weak picture of the Orb working.

The page already has a stronger picture of the same card: the recorded portfolio run, titled "Finish the SMASHED running loop," whose visible lines are sentences about the work and whose result is a pull request. Getting that picture on screen is a mode switch. It does not need a code change.

A live pass on `Pain-Point-Pipeline/amp-fit-v2` still ends by asking whether to connect the machine that holds the 10d study or to defer. Ledger rows 12, 23, 27, and 30 are that question. Typesetting will not turn it into finished work. Row 30's graded limitation stands: the options offer connect or defer, and retiring the September 12 direction is omitted.

## What the screenshot is

Live mode on `http://127.0.0.1:8177/amp-fit.html`, run `91257fba-cf39-4d9e-8831-2a2a2386807c`, thread `T-01a0c5b7-8907-73c6-9e68-ab765602d449`, ledger row 30. The server was answering on that port while this note was written. Chromium was not running, so this note was checked against the stored events and the page source, not against a fresh screenshot.

The card title is the literal string `AMP Fit pass · amp-fit-v2`. Live mode sets it in `site/amp-fit.html` and the runner stores the same string. It never becomes the job the Orb inferred.

Assistant text is split on blank lines into separate events (`scripts/amp-fit/events.mjs`). The stage is a bottom-pinned window. Its height is the newest paragraph plus 64 pixels, and at least 235 pixels. A mask fades the top 54 pixels. The newest paragraph is painted `#f6fff5`; older paragraphs are `#d1ddda`. `overflow-wrap: anywhere` may break a token in the middle, which is why the thread id renders as `T-` and `needs-decision` renders as `needs-` / `decision`.

Pass 30's message events, in order:

1. "I'll load the amp-fit workflow and repository rules, then check what work this pass is authorized to finish." (108 characters)
2. "The trail points to finishing the already-directed 10d field study: …" (373 characters)
3. `needs-decision: Connect the evidence-holding machine for the already-directed 10d continuation, or defer this pass? decides: Daniel.`
4. `Because:` the September 12 commit and the later repairs
5. `Options:` connect a runner on that machine, or defer
6. `Considered:` PRs #27 and #28
7. `Waiting on you:` Daniel provides the execution environment
8. `Noticed:` nothing changed; the freeze list; the rule files read
9. `Checked:` the command inventory in the screenshot
10. `ledger: | 30 | 2026-09-21 | … | needs-decision |  |  |  |  |  |`

Events 9 and 10 are the two paragraphs in the screenshot. The decision sentence is event 3. By the time the ledger line arrives it has been pushed above the window. Eight tool events sit between the job sentence and the decision, so the job sentence is above the window as well.

The right-hand column already receives event 3. On a non-PR finish it sets the heading to "An owner decision is needed." and sets the body to the first line of the outcome. The screenshot is cropped to the card, which is the part still showing the receipt.

While the pass is running, the same window shows shell commands. Inputs of 200 characters or less are shown whole on the stage; longer ones are cut with an ellipsis. Several commands in this run include `/home/danielkitchen/amp-fit-v2-work/…` inside that first 200 characters. View activity keeps the full command. Raw command output is already omitted.

The next Start on this page would launch `n=` as a UTC timestamp `YYYYMMDDHHmmss` (`demoPassId` in `scripts/amp-fit/runner.mjs`). The ledger line in that thread would be longer than row 30's. The proof ledger is not written by this button. As of this note, the open pull requests on `amp-fit-v2` are `cursor/*` branches. The launch refusal checks the `amp-fit/` prefix only, so those pulls do not block Start.

## Bounds that apply to every option

- The published skill must remain byte-for-byte identical to `skills/amp-fit/SKILL.md`. The launcher compares them in `scripts/amp-fit/client.mjs` and refuses Start when they differ.
- The `ledger:` line stays in the thread, last, so `sed -n 's/^ledger: //p'` still appends a row. The demo button still does not append one.
- The page does not invent a sentence, a job, or a pull request. Every word on the card is a stored event, or a label already on the page.
- View activity keeps the full event list, in order, including commands, `Checked:`, and the ledger line.
- Recorded playback of the SMASHED run keeps its current excerpts, timing, and title.
- Launch prompt, repository, open-PR refusal, session database, and owner-grade behavior stay as they are.
- Grades, scores, and "useful" do not appear on the card.

## Option A — rest the finished card on the decision sentence

**What the room sees when a live pass ends without a PR.** The bright paragraph is the Orb's own `needs-decision:` or `empty:` line. Above it, inside the same window, is the last ordinary prose sentence (for pass 30, the 373-character trail sentence). `Because`, `Options`, `Considered`, `Waiting on you`, `Noticed`, `Checked`, and `ledger:` are in View activity only.

**What the room sees while the Orb is working.** Unchanged: each new sentence and each command still enter at the bottom.

**At the moment the decision arrives.** Tool rows leave the card and remain in View activity. The card jumps from the latest command to the two sentences. That jump is the cost of showing commands during the run and a sentence after it.

**Scope.**

- `portfolio-site/site/amp-fit.html`, in `deliver` / `eventElement` and the feed CSS.
- A message is the terminal sentence when its text starts with `needs-decision:` or `empty:`.
- A message is a receipt when its text starts with `Because:`, `Options:`, `Considered:`, `Waiting on you:`, `Noticed:`, `Checked:`, or `ledger:`.
- Receipts are appended to the history dialog and omitted from `#af-track`.
- When the terminal sentence is appended, tool and tool-result nodes already on the track are hidden. They stay in the history dialog.
- The foot count still counts every event, so the number matches View activity. Receipts do not play the slide animation.
- No change to `events.mjs`, the runner, the store, or the result column. The column will repeat the same opening sentence it already shows. Leave that repetition.

**Negative effects.**

- The card no longer ends on the last line the Orb wrote. Someone comparing the card to the thread will find the receipt one click away, in View activity, and in the thread.
- Pass 30's Options line, the one that omits retiring the direction, leaves the card. The question stays. The incomplete menu is visible only in View activity.
- The `Because` links leave the card with it. The decision sentence names the machine and Daniel; it does not contain the September 12 commit URL.
- If a future pass puts the decision and the ledger in one paragraph, the splitter will not separate them, and the whole paragraph stays on the card. Pass 30 split them. The filter applies only when the event text itself starts with the prefix.
- A pass that opens a pull request does not emit `needs-decision:` or `empty:`. Its commands stay on the card until a later message pushes them up, which is today's behavior. Option A does not clean the success path.
- Hiding the tool rows at the end removes them from the card in one step. Pause/resume and refresh rebuild the track from stored events, so the resting rule has to run again on replay or the refresh will show the commands.
- The recorded SMASHED excerpts do not start with those prefixes, so their playback is unchanged only if the filter is prefix-based. A filter that hides every line containing the word "ledger" would be the wrong filter.

## Option B — put the inferred job in the title, once

**What the room sees.** The title stays `AMP Fit pass · amp-fit-v2` during the run. When the ledger line arrives, the title becomes the request cell with `inferred:` removed and the first character capitalized. For this run that is `Finish directed 10d study`. It does not change again. Recorded mode keeps "Finish the SMASHED running loop."

**Scope.** The ledger event handler in `site/amp-fit.html`, including when Option A does not place that event on the track. Read cell 4 by splitting on `|`. Accept it only when there are at least seven cells and the cell has no newline. Otherwise leave the stub.

**Negative effects.**

- The title moves once, at the end. The design asked for a fixed title that names the assignment. This is that assignment, learned when the Orb writes it down.
- A wrong inference becomes the title for the rest of the viewing. This run's cell matches the prose sentence.
- A `|` inside the request cell shifts the columns. None of ledger rows 1–30 have a pipe in the request. If a cell fails the guard, the stub remains, which is the current title.
- The title does not include the thread id, the timestamp `n`, or `needs-decision`.

## Option C — keep tokens whole

**What the room sees.** `needs-decision` and the thread id wrap at spaces. A token wider than the column can still break, so a long id on a 390px screen can still split.

**Scope.** In `site/amp-fit.html`, change `.af-event` from `overflow-wrap: anywhere` to `overflow-wrap: break-word`. History uses the same class.

**Negative effects.**

- The ledger line is still the resting paragraph if Option A is not done. The line is readable as a line and still reads as a receipt.
- A single token wider than the card breaks inside the word, as it does today. The feed stays `overflow: hidden`, so the page does not gain a horizontal scrollbar.
- This is worth doing with A or without it. It does not change which paragraph the window rests on.

## Option D — keep the home-directory path off the card

**What the room sees during the run.** A command is shown as it is today, except an absolute path under `/home/danielkitchen` is replaced with `…` on the stage and in View activity. The stored event and the thread keep the real path.

**Scope.** Display only, in `eventElement` in `site/amp-fit.html`. Not in `redact()` in `events.mjs`, so reconnect cursors and stored source keys stay stable.

**Negative effects.**

- View activity no longer matches the thread for those characters. The thread link remains the original.
- Option A's resting card already hides commands. The path is still one click away in View activity until this option is applied.
- A path outside that prefix, or a path written without the `/home/danielkitchen` prefix, still shows.

## Option E — open on the recorded run

**What the room sees.** The card title is "Finish the SMASHED running loop." The lines are the selected Orb sentences and two real commands from pass 13. The result column fills with PR #2 when the recording reaches it. The mode label says "Recorded run · 20 September 2026."

**Scope of doing nothing.** The selector already has this mode. Choosing Recorded does not launch, steer, or stop an Orb.

**Scope of opening there.** `initializeLive` in `site/amp-fit.html` currently calls `selectMode('live')` when the local session answers. Leaving the visitor on Recorded is that one call. Start then plays the recording.

**Negative effects.**

- The label says it is a recording with compressed timing. A visitor who wants a live Orb uses the selector.
- Switching to Live and pressing Start launches a new high-mode Orb on `amp-fit-v2` with no work directive. The likely resting card is another 10d question, and the ledger line in that thread uses the timestamp `n`.
- This option does not change the live card. After a live pass, the screenshot's frame is still what Live rests on, unless A is also done.

## Option F — typeset the ledger on the card

**What the room sees.** The pipe line becomes labeled fields: job, repository, outcome. The raw line remains in View activity.

**Scope.** A renderer in `eventElement` for events whose text starts with `ledger:`.

**Negative effects.**

- The receipt becomes the designed surface. The thing the room reads is still "finish directed 10d study" and "needs-decision."
- A pipe inside the request mis-labels the outcome. The guard in Option B avoids showing a bad parse; a typeset card that guesses is worse, because it looks official.
- The next live `n` is a 14-digit timestamp. A typeset card would display that number as if it were a pass number.
- This option fights the pitch. The ledger is the proof row. It is not the product on the card.

## Option G — change the skill so the Orb speaks a demo sentence last

**Do not do this for the demo.**

The status order is the owner's one-minute read, and the ledger line is specified as the last line. `SKILL.md` is 65 lines; the cap in `README.md` is 80. The launcher refuses Start when the published file differs from the canonical file. Republishing would change every later real pass, not just the card. A pass whose diff is in the amp-fit tree is not a pass and gets no ledger row.

The card can choose which of the Orb's sentences to rest on. The Orb should keep writing the receipt.

## If one change is made before the demo

Do A, B, and C together, and leave D, F, and G alone.

The finished live card then shows `Finish directed 10d study` as the title and the Orb's decision sentence as the bright paragraph, with the trail sentence above it. Commands, the check inventory, and the ledger line stay in View activity, verbatim. Tokens wrap at spaces. The recorded run is untouched. Start, the prompt, the open-PR refusal, and the skill bytes are untouched.

That card will still ask Daniel to connect the 10d machine or defer. Option E is how the room sees an Orb finish a job instead.

## Files a change would touch

| Option | File | Left alone |
| --- | --- | --- |
| A, B, C, D | `portfolio-site/site/amp-fit.html` | `events.mjs`, runner, store, skill, `LEDGER.md` |
| E, default mode only | the `selectMode('live')` call in that same file | the recording JSON |
| F | that same file | the ledger line in the thread |
| G | `skills/amp-fit/SKILL.md`, then a republish | out of scope |

## Check before calling any of this done

Reload the completed run. The card shows the decision sentence and the trail sentence, and does not show the ledger line. View activity still contains `Checked:` and the ledger line character for character. The recorded mode still plays the SMASHED excerpts and still reveals PR #2. A 390px width does not scroll sideways. Refresh and display-pause rebuild the same resting card. No new Orb starts during that check.

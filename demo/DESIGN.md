# AMP Fit demo — design and first build

Owner-directed design, 2026-09-21. Intended home: an `/amp-fit` page in Daniel's existing portfolio. This document maps the proposed page and implementation; it does not record a live run or a deployment.

## The visitor's journey

The visitor understands the assignment, clicks **Start Demo**, watches the Orbs do the work, and opens the resulting GitHub pull requests. The skill explanation and performance evidence remain available on the same page while the work runs.

Use Daniel's existing portfolio navigation and plain HTML, CSS, and JavaScript structure. Daniel requested the exact Amp green: use Amp's `#091C1E` dark shell and `#0C1516` dark surface. The Figma reference matches the latter. Both values were checked against Amp's website on 2026-09-21. Keep these colors local to this page.

## Confirmed Orb design

Reference: [AMP Fit Agent Work](https://www.figma.com/design/HaZbmea9rFCF8ab273cqEE/AMP-Fit-Agent-Work?node-id=0-1).

- Use the original white, two-eyed Orb artwork. Its reference layer is `6:31`; the heading and activity text are in `6:35`.
- The Orb identity and **work title** remain fixed. The title describes the assignment; it is not replaced by every tool action.
- The text below the title is the agent's changing activity.
- Preserve the actual activity's wording, length, and pauses when streaming live. The illustrative preview does not prescribe messages or scripted steps.
- New activity enters at the **bottom** and pushes older activity upward.
- Older activity fades into the background at the **top** of the activity area. Apply the fade only to the activity, never the title or Orb.
- Keep the newest activity fully readable. Preserve the full activity history behind a separate detail view.
- Represent actual Orbs. Visual stages within a single run must not imply that additional agents exist.

The initial interaction preview uses labeled sample activity. It demonstrates this layout and motion, without launching an Orb.

## Page map

| Area | Content and behavior |
| --- | --- |
| Introduction | AMP Fit, a short statement of what the skill finishes, and a route back to the portfolio. |
| Demo setup | The named scenario, repository, and expected outcome, followed by **Start Demo**. Show whether the selected experience is live or a recorded replay before starting. |
| Running work | The primary surface: one activity view per actual Orb, using the confirmed design above. Show genuine queued, running, waiting, completed, or failed states. |
| Pull requests | Results alongside the running work on desktop and below it on mobile. Each result names what changed, shows available verification, and links to the actual GitHub PR. |
| How AMP Fit works | A short explanation: recover the owner's unfinished objective, choose the work that addresses it, make and verify the change, and return one PR or an actionable status. Link to the skill. |
| Evidence | Recorded field outcomes with their sources, followed by the regular-Orb comparison when paired results exist. Show the period, sample size, and measurement definitions. |

Keep the initial viewport centered on the assignment, Start Demo, and the Orb surface. Avoid a wall of metrics above the demonstration. The PR area begins as a clear pending state and fills only when results exist.

## Demo behavior

1. **Ready:** explain the selected assignment and mode. The activity area is ready but does not pretend work is already happening.
2. **Starting:** acknowledge the click immediately and show the actual launch state. Repeated clicks must not create duplicate runs.
3. **Running:** update activity from observed messages and tool events. Keep the work title fixed. Expose details without overwhelming the main view with raw command output.
4. **Result:** attach verified PR links to the Orb that produced them. A successful agent turn alone does not prove that a PR exists or that its checks passed.
5. **Other outcomes:** show an owner decision, no grounded work, or an execution error honestly. The AMP Fit skill can legitimately finish without a PR.
6. **Return visit:** reconnect to an existing live run instead of starting another. Preserve completed results for inspection.

Proposed presentation mode: support both live execution and a clearly labeled replay of a captured run. The default mode is still to be chosen; no answer to that earlier question has been assumed. A live failure must remain visible rather than silently switching to replay.

## Build shape

- **Portfolio page:** the existing static site hosts the UI. Reuse its navigation, visual tokens, and access gate.
- **Run service:** a server-side job runner launches the approved scenario, owns the run lifecycle, and keeps credentials off the page. Its hosting location remains to be selected.
- **Activity record:** store ordered events with a run ID, Orb/thread ID, time, type, and display text. A live event feed and recorded replay drive the same UI.
- **Results:** associate GitHub PRs with the correct repository and run, and read their real state. Private PRs require the visitor's own GitHub access or a separately prepared shareable demo repository.
- **Read access:** give the page only the information needed for this demo, rather than publishing entire private threads or arbitrary command output.

The verified Amp integration is `amp -ox` with `--stream-json` and an explicit project. The stream includes messages, tool activity, and final results. Retaining the thread uses `--no-archive-after-execute`. See [Spawning Orbs](https://ampcode.com/docs/cli/spawning-orbs) and [Streaming JSON](https://ampcode.com/docs/cli/streaming-json).

The browser visual is driven by reported activity, rather than invented internal reasoning. Actual execution, reconnection, and terminal outcomes must be verified against an approved Orb before the live experience is described as working.

## Evidence available now

Snapshot of `LEDGER.md`, rows 1–29, read on 2026-09-21:

- 29 recorded, owner-graded passes across five repositories.
- 20 merged PRs, one PR closed as the wrong job, five questions graded `asked-right`, and three outcomes graded `empty-right`.
- 335 total minutes of owner review, decision, and correction effort across those passes.
- 1,005 minutes of owner-estimated time saved on merged work. This is an estimate recorded by the owner, not measured runtime or a comparison with regular Orbs.

The ledger has no regular-Orb baseline, elapsed run durations, or per-pass cost column. Do not fill those gaps with invented values or present a relative improvement from these rows alone.

For the comparison, use matched starting commits, owner objectives, context, resources, and verification. Isolate the runs and ensure the baseline cannot load the AMP Fit skill through personal or project skill configuration. Record the differing invocation, both outcomes, elapsed time, available usage/cost, and owner review effort. Show individual paired outcomes and the sample size; a demonstration run is not a broad performance claim.

## Implementation order and acceptance

1. **Page and replay:** build the responsive page and confirmed activity behavior. Use clearly labeled fixtures while preparing a captured, shareable run. Include the skill explanation and sourced ledger evidence.
2. **First live path:** connect one approved scenario end to end: Start Demo → actual Orb events → verification → actual PR or truthful alternate outcome. Check this path early, before expanding the number of Orbs.
3. **Presentation reliability:** verify duplicate-click prevention, reconnecting, waiting/error states, complete activity access, and readable desktop/mobile layouts. Preserve the same event format for replay.
4. **Comparison:** collect and display paired regular-Orb results separately from the existing field ledger. This work does not block the page, replay, or live integration.
5. **Publication:** show the concrete working result before the portfolio's explicit deployment step. No deployment is included in this design task.

Before launching real demo work, select the scenario and repository, the intended visitor access, and the run service host. These choices do not block the UI or fixture-based integration work. The existing portfolio checkout has unrelated edits; implementation must preserve them and use disjoint files or an isolated checkout as appropriate.

Daniel has left the live repository choice open. Design the live integration to accept a selected repository; the recorded portfolio scenario is not a restriction on future runs.

## First local implementation

The first full page is `../portfolio-site/site/amp-fit.html` relative to the amp-fit repository root. Its data files are `site/data/amp-fit.json` and `site/data/amp-fit-pr.json`, with the original icon at `site/images/amp-fit-orb.png`. Shared portfolio files remain untouched.

The page replays selected original assistant paragraphs and two actual tool calls from pass 13, thread `T-01a0bef2-e755-70db-81a9-b89a3b489c6a`. It uses compressed playback timing, clearly labeled; original message timestamps were unavailable in the markdown export. The resulting [PR #2](https://github.com/iamdanielkitchen/portfolio-site/pull/2) was checked through GitHub and is merged. The page reveals it when the recording reaches the original PR message. It does not launch new work.

The local data includes a thread-export SHA-256, source block references for each event, and a commit-specific ledger link. `demo/export-recording.py` regenerates it from that thread's markdown export, a verified PR snapshot, and the current ledger. It excludes the original attachment URL and does not publish the raw thread export.

Local preview: serve the portfolio's `site/` directory and open `/amp-fit.html`. Playback has pause/resume/replay, pauses while offscreen, retains the full selected activity in a detail dialog, and shows the ledger rows behind a disclosure. No portfolio deployment has been performed.

Checked locally: original excerpt wording and ledger totals; complete playback and PR reveal; clean replay; pause/resume; activity dialog and Escape/focus return; a 390px layout with no horizontal overflow and the newest paragraph below the fade; all 29 evidence rows; and exact rendered Amp shell/surface colors. The browser reported no warnings or errors during these checks.

## PR handoff implementation

The result remains pending until the recorded Orb message contains the delivered PR. At that point the page fetches the separate GitHub snapshot, verifies its repository and branch against the recording, and fills the card from the response. The title, PR number, state, description and file counts are no longer hardcoded in the page. A result fetch failure offers Retry without restarting the recording.

**Review changes** opens an on-page dialog with the PR's explanation, its reported verification, actual GitHub check status, and expandable text diffs. The full PR description and GitHub link remain available. Source text and patches are rendered as text, never interpreted as HTML. Missing/binary patches and shortened previews are labeled. The recorded PR currently has two files, 101 additions, and no GitHub CI checks; the Orb's reported browser verification is shown separately. Its merged state is dated as a GitHub snapshot.

The portfolio now contains these integration files:

- `functions/lib/amp-fit-results.js`: discovers GitHub PR URLs in normalized Orb messages/tool results, verifies the expected base repository, head repository, branch and creation time, and optionally verifies the head commit. If the link is missing, it searches that run's branch. It rejects ambiguous results and checks the head again after reading files and checks. Only GitHub GET requests are made.
- `functions/api/amp-fit/runs/[id]/result.js`: reads a server-owned, explicitly published run record by opaque ID. The existing portfolio middleware protects the route. Browser input cannot choose a repository, URL or credential. The route returns 503 until the future run store is configured; it is not connected to a live runner yet.
- `scripts/amp-fit-capture.mjs`: captures a real result through the same resolver using authenticated, read-only `gh api` calls. It exports no token.
- `tests/amp-fit-results.test.mjs`: covers recorded-message resolution, missing links, branch/fork/repository mismatches, old PRs, pending and no-PR outcomes, changed heads, partial files/checks, GitHub access errors, and the authenticated/unauthenticated route.

The runner will write `AMP_FIT_RUNS` entries under `run:<id>` with this contract (example placeholders):

```json
{
  "publishResult": true,
  "repo": "owner/selected-repository",
  "headRepo": "owner/selected-repository",
  "branch": "unique-branch-for-this-run",
  "startedAt": "2026-09-21T12:00:00Z",
  "events": [{"type": "message", "text": "Actual Orb message"}]
}
```

`headSha` can bind the expected commit when the runner knows it. `outcome: "no_pr"` is an explicit terminal outcome; completion alone never proves a PR exists. The runner may persist the resolver's `result`; the endpoint accepts a matching ready result for up to 60 seconds and otherwise reads GitHub. The endpoint does not rewrite active run records. GitHub credentials belong in the server's `AMP_FIT_GITHUB_TOKEN` secret. No KV binding, secret or production configuration has been created in this task.

To refresh the local recording, supply the actual run identity/events in a local JSON file, then run from the portfolio checkout:

```sh
node scripts/amp-fit-capture.mjs /path/to/run.json site/data/amp-fit-pr.json
```

Then, from the amp-fit checkout:

```sh
python3 demo/export-recording.py /path/to/thread.md ../portfolio-site/site/data/amp-fit-pr.json ../portfolio-site/site/data/amp-fit.json
```

Validation: the resolver fetched the actual PR through GitHub; all 14 targeted integration tests passed; Wrangler compiled the Pages Functions. Browser checks covered pending → result, on-page explanation and diff expansion, literal HTML appearing as code, mobile containment and diff scrolling, Escape/focus return, and an isolated 503 → Retry → actual result path. No real Orb was launched, merged or deployed by these checks.

## First live connection — delivered locally

Daniel selected a fresh pass on `Pain-Point-Pipeline/amp-fit-v2`, with no directive, and local hosting first. The portfolio now provides `npm run demo:live` at `http://127.0.0.1:8177/amp-fit.html`. See `../portfolio-site/scripts/amp-fit/README.md` for setup, API, state and recovery details.

The local Node service serves the page and authenticated launch/read endpoints together. It uses the existing Amp project, streams actual messages/tool activity, and stores normalized events outside the repositories in private SQLite state. The prompt is exactly `amp-fit pass. n=<row> repo=Pain-Point-Pipeline/amp-fit-v2`; it has no `request=` field and no automatic follow-up steering. Browser refresh and display pause do not launch or stop an Orb. The existing recording remains a separate mode. Credential patterns and raw tool output are omitted from the activity view.

Real acceptance run: pass **30**, [source thread](https://ampcode.com/threads/T-01a0c5b7-8907-73c6-9e68-ab765602d449), launched through Start Demo on 2026-09-21. The thread confirms high mode, the intended project, activation of `amp-fit`, and precisely one user prompt matching the invocation above. It returned `needs-decision` for access to the existing 10d plan/evidence machine. No PR was produced; the default branch remained `38b7757c1b4161d9980d9c0a59568da5d2dc9433`. Its ungraded result is recorded in ledger row 30.

Verified: live activity, display pause with 21 updates retained and caught up, same-thread refresh, completed-run persistence after server restart, recorded/live mode switching, and mobile containment with the newest activity below the fade. The raw export uses a different tool-result shape from streaming JSON; normalization handles both, with source-event deduplication rather than replaying a new run.

## Publication and ownership

From 2026-09-21, major updates to this demo page are maintained from the amp-fit checkout. That covers the page layout, the recorded run, the evidence snapshot, and publishing those files to the portfolio's Cloudflare Pages project.

The public page is https://painpointpipeline.com/amp-fit. When the runner on this machine is up, Start Demo launches one real high-mode Orb on `Pain-Point-Pipeline/amp-fit-v2` with no work directive. The 20 September recording stays available in the mode selector and is what visitors get if the runner is down. There is no `AMP_FIT_RUNS` namespace and no GitHub token in Cloudflare. The runner keeps using the Amp and GitHub CLIs already signed in on this machine. Public launches stop after eight new Orbs in a UTC day. An Orb that is already running can still be watched.

Portfolio passes leave these files alone unless Daniel asks otherwise:

- `site/amp-fit.html`
- `site/data/amp-fit.json`
- `site/data/amp-fit-pr.json`
- `site/images/amp-fit-orb.png`

The homepage card lives in `site/index.html` and is part of the same page. The regular-Orb comparison remains separate. Completing the Orb's proposed 10d study work is not a prerequisite for the demo page and was not performed by this task.

# Amp Fit v1–v4: postmortem, and the decision for what comes next

Date: 2026-09-19. Written by a Claude Fable 5.1 session working with Daniel Kitchen, from the four trees (`SMASHED/products/amp-fit` remnants, `amp-fit-v2`, `Amp_Fit_v3`, `Amp_Fit_v4`), the private work roots (`~/amp-fit-v2-work`, `~/amp-fit-v3-work`, `~/amp-fit-v4-work`), the Amp account's thread and project lists, and ampcode.com documentation as of today. Status: a record. It explains why the `amp-fit` tree has the shape it has. `../README.md` is the executable plan; this file is the reasoning behind it.

## 1. Summary

Amp Fit has had one purpose since v1: show a repository owner grounded work that Amp could take over, let them accept it, and have Amp deliver it. Four versions were built in about three weeks (v2 through v4 fit in fifteen days). Each version built an evaluation and governance apparatus first so that no claim could be fabricated, gated the product on that apparatus, and then could not complete the apparatus. No real owner ever accepted real Amp work through any version. The apparatus was never the product; it consumed all the attention the product needed.

Meanwhile the two halves that matter were each shown to work in isolation. Amp finds substantive work on real repositories when asked directly (twenty validated proposals on psf/requests, twenty-two on pallets/click, a real defect in a supplied comparator). Amp delivers pull requests with honest bodies when asked directly (two draft PRs on amp-fit-v2 on 2026-09-14). What never once happened is the third step: an owner reading the result and saying whether it was useful. The two PRs are still open and unreviewed five days later.

The decision is therefore to stop building apparatus. The product is a work pass: an Amp Agent Skill that carries the assignment, run on Daniel's real repositories, delivering PR-only, with Daniel's grade of each pass recorded in one ledger table as the only proof. Nothing else is built until the same limitation appears in two graded rows.

## 2. What Amp Fit is for, in the trail's own words

- v2 recommendation (`amp-fit-v2/docs/recommendations/amp-fit-v3.md` §1): "Amp Fit is two screens, one server, one palette, one primary button. An owner consents a tree. Screen 2 shows grounded work Amp can start on that tree, or the exact empty copy. Accept always opens a pull request on a fresh work branch. Never writes the owner default branch. Empty first-session is success."
- v3 charter (`Amp_Fit_v3/CHARTER.md`): "consent a real tree → native Astra discovery → honest empty Screen 2 or grounded proposals → Skip or explicitly selected native work."
- v4 product sentence (`Amp_Fit_v4/METHOD.md`): "from the owner's unresolved objective and the whole work trail, infer the continuing responsibility, do and verify the authorized work, and leave human decisions explicit; Screen 2, when it exists later, is that same method's card."
- Daniel, preserved in `Amp_Fit_v4/docs/history/initial_checkpoint.md`: "Knowing what they do is not a problem to solve. How we help them is the problem to solve." And: "the V2 effort took more than a month before it could be tested and verified. The lesson for V3 is to exercise a complete, meaningful path early, without building a general orchestration program first."

The user is a repository owner. The unit of value is one accepted piece of work. No version wrote down a customer, a buyer, or a business model; the word "Sourcegraph" appears in none of the trees. Whether Amp's makers are an audience for the resulting ledger is an open decision, recorded in §14.

## 3. Timeline

| Version | Dates (2026) | Size | Ended by |
|---|---|---|---|
| v1 | before Sep 2 | untracked files, now gone | fabricated evidence (audited Sep 2) |
| v2 | Sep 4 to Sep 16 | 499 commits, 9,457 files | supply halt, census in the critical path, capability never measured |
| v3 | Sep 12 to Sep 16 | 66 commits, 515 files | its own gates rejected every real finding; conclusion that twelve categories were the wrong shape |
| v4 | Sep 16 to Sep 18 | 19 commits, 256 files, about 16k lines mostly Markdown | proof-only labs; a selection error; a contract freeze with no owner pass |

Total real Amp cost across all native runs is negligible under the current subscription: the completed v4 CAL run cost $0.08 for ten minutes of High/`gpt-6-astra` work. Human and agent attention, not money, was the resource each version exhausted.

## 4. The four versions

### 4.1 v1: two screens, twelve categories, and minted capability

v1 existed as untracked files under `SMASHED/products/amp-fit`; no repository or history survives. What survives is v2's read-only audit of it (`amp-fit-v2/PLAN.md` §2–3, measured 2026-09-02) and the visual specs at `SMASHED/spec/drafts/amp_fit_*.md`. Its thesis was already the product: Scan Repo, Screen 2 cards of what Amp can do, Accept opens a PR, a ternary `can_perform` per work category.

It died of fabricated evidence, in v2's words: "Corpus rows are directory listings… 402 rows in ~30 minutes"; "The work taxonomy is circular. `typical_artifacts` are V1's own fixture filenames"; "Capability unmeasured, then mis-minted… `yes` on `hard_diagnosis_viability` and plan execution from PRs whose only files were `.agents/` scaffolding"; "`amp.dangerouslyAllowAll: true` in settings and `--dangerously-allow-all` appended in Accept". It was preceded by a separate "repo owner value predictor" program (`SMASHED/docs/plans/2026-09-04-amp-repo-*.md`), halted the same day it started.

v2 kept from v1 what is still worth keeping: two screens, PR-only Accept, never writing the default branch, empty-is-success, mirrors rather than touching strangers' repos.

### 4.2 v2: the finished product, built as law

Thesis (`amp-fit-v2/PLAN.md` §1): "A from-scratch build of the finished Amp Fit product — what the WB Amp Fit teams would have produced if every team had done its job perfectly." Three questions: Q1 what repositories exist and how people work (a GitHub census, `field/`, 7,764 files); Q2 what Amp can really do (a work bank of validated tasks and a lab, `workbank/`, `lab/`); Q3 what to offer this repository (`predict/`, `web/`, `accept/`). Governance: `LAW.md` fences, `FREEZE.json`, `RUNBOOK.md` kill switches K1–K7, coordinators, tickets, and status-Markdown gates ("no open ticket = no write"). Up to 21 concurrent native Amp workers implemented the packets.

What was observed:

- The census enriched 484 repositories with 10,884 REST requests and produced nine shipping rules, all `ship: false`; the live 10d harvest filled `landing_practice` for only 41 % of rows, so clustering could not learn how people land work (`amp-fit-v3.md` §3).
- The lab recorded 57 trials on real OSS mirrors: `cli_execute` 0 of 32 succeeded (16 timeouts from an unanswered guarded-write prompt, "ui_prompt_stall"), orb 4 succeeded; read-only diagnosis 6 of 8 fair trials succeeded. Every one of twelve categories stayed `can_perform: unknown` (`lab/out/capability.json`, `lab/out/cost_report.md`).
- The work bank ran out of validated tasks on Sep 7 (decision 59 tried to substitute cached tasks; decisions 60/61 voided it). The `amp-fit-v2-supply-halt-79d2` directory is a worktree of that abandoned branch.
- Screen 2 never legally showed a non-empty offer: `predict/scan.py` raised HTTP 400 when `field/out/archetypes.json` was missing, and the file could not exist without the census. The only Accepts were on four throwaway repositories with planted `amp_can_perform: "yes"`, since deleted (`docs/recommendations/48h-wrap.md`). Every receipt in `accept/receipts/` is a refusal.
- Grader calibration worked: blind rubric grading by Daniel, Grok and Astra reached κ = 1.0 on ten trials after one rubric rewrite.

v2's own diagnosis on Sep 12 (`docs/recommendations/amp-fit-v3.md`): "That is the architectural mistake: a GitHub census was wired into the critical path of a product that does not use it to choose work." And: "Keep the purpose. Invert the dependency… this tree, this pointer, this lab proof, or empty." Phase 7, owner trials on fifteen consented repositories, was never reached.

### 4.3 v3: the 48-hour spike that ran on real repositories

Thesis (`Amp_Fit_v3/CHARTER.md`): consent a real tree, native High/Astra discovery across twelve categories (`failing_check_repair`, `missing_test_coverage`, `reported_bug_fix`, `hard_diagnosis_viability`, `review_second_opinion`, `parallel_readonly_audit`, `mechanical_plan_execution`, `overnight_unsupervised_edit`, `tight_project_skill`, `event_driven_failing_check`, `standing_scheduled_wake`, `cheap_docs_polish`), Screen 2 proposals, Skip or Accept, PR delivery through Amp's Custom Ship. A Python stdlib server on `127.0.0.1:8799`; Amp invoked as a subprocess with `-ox --mode high`.

What was observed:

- Real native scans on real OSS repositories: sindresorhus/p-limit 10 raw / 10 validated / 10 displayed; pallets/click 23 / 22 / 22; go-chi/chi 28 / 26 / 26; psf/requests 22 / 0 / 0 in the campaign (citation validation rejected all 22 and the screen then painted the empty-success copy), then 20 / 20 / 20 in the orientation experiment: 58 minutes, 29 native child threads plus 17 helpers, $0 (`docs/amp-native-workflows/14-screen-two-experiment-results.md`).
- The Codex review of those twenty proposals (`docs/amp-native-workflows/16-preserved-proposal-review.md`): seventeen technically supported candidates (test gaps, remaining work on open upstream PRs, documentation defects, a source/docstring mismatch), two blocked, one unresolved. "The list offers technically plausible work, but it does not rank these outcomes against a stated repository-owner goal."
- Daniel's private repository AJO (5,403 files) was scanned on Sep 13. Screen 2 showed "Amp has nothing it can start here without you designing the work first," by design: detector G3 required `can_perform ∈ {yes, partial}` and a shipped rule, and neither ever existed (`~/amp-fit-v3-work/clones/ajo-scan-20260913T212036Z-22ee55/report.md`).
- Zero Accepts on any real repository. `LIMITATIONS.md`: "'V3 shipped' is false." "No real application repository has been Accepted."
- Outside the product path, on Sep 14, raw native Amp given a one-page request ("Find and repair current failing checks in Pain-Point-Pipeline/amp-fit-v2… deliver useful PRs through the configured PR-only route") delivered two draft PRs, #27 (+7/−1) and #28 (+100/−9), each with a complete body: repair, verification commands and results, scope and limitations, "Do not merge automatically." Both are still open and unreviewed on 2026-09-19.

v3's conclusion on Sep 16 (`docs/amp-native-workflows/24-automation-feasibility-v2.md`): "live Screen 2 will not be a twelve-category list… today's post-audit compiler… is expected to be replaced, not adapted." The twelve categories were a menu, not a discovery method. Method work moved to v4.

### 4.4 v4: the labs, the selection error, and the contract

Thesis: first, an "automation feasibility" experiment split into D1 (can a six-phase controller, typed artifacts, probes, a bounce and a Screen 2 card run together on Amp), D2 (does Amp choose useful assistance; do phases earn their keep) and D3 (publication contract), each a synthetic lab with hidden oracles; then, after Sep 17, `METHOD.md`: the agent infers the continuing responsibility from the owner's unresolved objective and the whole work trail, does and verifies the authorized work, and leaves human decisions explicit.

What was observed:

- The Orb transport works. `native/amp.py` launches with `amp -ox --mode high --project <id> --no-archive-after-execute --visibility private`, continues with `amp threads continue <T> -ox` (the argument order bug is fixed in `f95712a`), exports, observes settlement of owned child threads and model identity, and recovers from an interrupted send without resending (`native/checkpoint.py`, 173 tests).
- Two completed real Orb runs on Sep 17, both on synthetic fixtures: CAL reached `supported_offer` after Amp found a real defect in the supplied comparator (conflicting duplicate IDs made the output depend on row order) and the host re-executed the exported fix against hidden inputs; R-path reached `no_suitable_candidate` after injected evidence showed the work was already automated. $0.08 and ten minutes each; about 590k input tokens, 91 % cache reads (`~/amp-fit-v4-work/review-latest-20260917/review.md`). The same review found the rendered card was 922 words, mostly accumulated assumptions, and still asked questions the mechanism had already settled.
- Sep 17, the selection error: told "You have this repo. Do it yourself as if you're the amp agent," a Codex-hosted agent chose evidence-ID and CI repairs on an unmerged branch. Daniel corrected it. `docs/workflow-selection-error.md`: "the measurement-friendly representation selected the work, instead of the actual unfinished work selecting the approach."
- Sep 18: `METHOD.md` frozen as the contract (R1–R12, AE1–AE10). The same morning's 452-line "production work foundation" plan, with a SQLite work store and an Amp CLI coordinator, was explicitly not adopted. Two Claude-hosted agents then read the tree cold and declined the bait (a failing PR, three green PRs, runnable suites); one prepared the PR reconciliation that Daniel had already decided. PRs #3–#6 were closed.
- "Correction burden" was named the product metric with no definition and no recorded value. `docs/later/` holds about 4,600 lines of specs each stamped "not authorized to implement."

## 5. The invariant failure

Every version ran the same loop:

1. Build an evaluation and governance apparatus so that no claim can be fabricated: v2's LAW, census and lab; v3's citation validation, identity verification and detector G3; v4's D1/D2/D3 labs and the `method_proof: false` stamp on every artifact.
2. Gate the product on that apparatus: v2's archetypes 400 gate and `can_perform` floor; v3's G3; v4's "not proof, not Accept, not live" on every file.
3. The apparatus cannot complete: supply halt; identity readback not wired; all 22 citations rejected; "the public packet already contains the answer" (v3 stress audit S1).
4. So no real owner ever sees a real grounded offer, and no one accepts anything. Product value stays `unknown` by construction.
5. Redesign. Repeat.

The agent-level symptom Daniel named, agents choosing the gradeable adjacent task over the owner's real objective, is the same mechanism one level down. v1 fabricated evidence; v2 through v4 over-corrected into proof-before-product and starved the product of the only evidence that matters, which is a real owner accepting real work. Three further invariants: no customer or business model was ever written down; evaluation cost swamped product cost; and the only outputs that reached the owner's side of the loop, PRs #27 and #28, were never graded.

## 6. What demonstrably works and is kept

| Asset | Where | Evidence |
|---|---|---|
| Amp Orb transport: launch, continue, export | `Amp_Fit_v4/native/amp.py`, `argv.py` | two completed real runs |
| Settlement observation of owned child threads and identity | `Amp_Fit_v4/native/observe.py` | used on both runs |
| Durable checkpoint, never resend an uncertain send | `Amp_Fit_v4/native/checkpoint.py`, `docs/post-run-repair.md` | 173 tests; real recovery |
| Amp finds real work on real repositories when asked directly | v3 scans; CAL defect; PRs #27/#28 | observed |
| PR-only delivery via Custom Ship, never the default branch | v2/v3 `accept/`; `~/amp-fit-v3-work/experiments/native-real-work-v2-*` | two real PRs |
| The six-section offer shape | `Amp_Fit_v4/DESIGN.md`, `d1/render.py` | stable across v3 and v4; reused as the PR body headings |
| The assignment text | `Amp_Fit_v4/METHOD.md` "recurring assignment"; `docs/workflow-selection-error.md` four-step approach | two cold agents followed it and declined bait; now the skill body |
| The candid drift records | `cases/workflow-selection-error.md`, `cases/amp-fit-method-drift.md` (copied here) | the rails agents demonstrably read |
| Blind-rubric grading, κ = 1.0 | `amp-fit-v2/lab/out/cost_report.md` | reusable for a second grader after ten rows |

The transport and checkpoint code stays in the archived v4 tree, retrievable by path. The loop here calls the Amp CLI directly; a checkpoint or observer is built only when a graded row says one was needed.

## 7. What is dropped, and the honesty rules that survive

Dropped: the twelve-category taxonomy and the `compact`/`qualify`/`offer` compiler; the `field/` census, `workbank/` supply and `predict/` ranker; LAW, tickets, coordinators and status-Markdown gates; the SQLite/CLI coordinator plan; the six-phase D1 controller as a product loop; `can_perform` as a gate; planted fixtures and throwaway proofs; `FREEZE.json`/`STATE.json` proof flags; K4 resource gates, identity readback and preflight as product steps; Wilson intervals and `n ≥ 12`; citation validation and live-pointer re-dereference (a git conflict does that for free); the negation-banner style ("not proof / not authorized / does not establish") that opened every v4 file; Daniel-owned JSON go-ahead files (the launch line is the authorization); and "empty is success" as a slogan (an empty row is valid; three in a row is a stop signal).

Six rules survive, in `skills/amp-fit/SKILL.md`, because each blocks a specific v1 fabrication: PR only on an `amp-fit/<n>` branch, never the default branch, never merge; Amp owns permissions, no `dangerouslyAllowAll`, no edits to the target's Amp settings, owner never-touch lists are authority; the agent never writes a quality judgment about its own work; every verification claim names the command that ran; nothing mergeable means `empty` or `needs-decision`, never a padded PR; the amp-fit tree and Amp_Fit_v3 are never the target.

## 8. Platform facts that shape the path (verified 2026-09-19)

- Agent Skills: a directory with `SKILL.md` (frontmatter `name`, `description`; body instructions; scripts and references allowed; 200 files, 25 MiB). `amp skill add <owner/repo[/path] | git URL | local path> [--global]`. Discovery includes `~/.config/agents/skills/`, `.agents/skills/` in a project, `.claude/skills/`, and personal or workspace skill repositories, so one skill serves Amp and Claude Code. Sharing is a URL from Personal Settings > Skills.
- Plugins: TypeScript; events `session.start`, `agent.start`, `tool.call`, `tool.result`, `agent.end` (may `continue` up to five chained turns); `registerTool`, `registerCommand`, `registerSkill`; custom agent modes; `createWebhook` gives a durable capability URL per plugin and owning Orb thread. Distributed by URL. No official store documented.
- Execution: `amp -x` local, `amp -ox` in an Orb (returns at once; the thread keeps working); `--stream-json` and `--stream-json-input` for programmatic drive; `amp threads continue T-… -x|-ox`; `--mode high`; `--project`; `--no-archive-after-execute`. Local non-interactive execution stalled in v2 on permission prompts nobody could answer; Orb runs did not.
- Projects bind a repository to Orbs and hold shared settings; Custom Ship behavior drives PR delivery. The account already holds projects for amp-fit-v2, two for amp-fit-v3, eight OSS audit targets, and food-bridge-app (the ampfit2-lab mirror).
- Automations (ampcode.com/docs/orbs/automations): "Automations let an Amp thread continue working later or on a repeating schedule… The agent keeps the thread's context and history… If a run fails, Amp pauses the automation… Each thread can have one schedule." Recurrence is one sentence to an accepted thread. Built-in skills `building-schedules`, `building-skills` and `creating-webhooks` exist.
- Cost: negligible under the current subscription; the completed CAL run was $0.08.

## 9. The decision, and how the design disagreements were resolved

The product is a work pass, not an apparatus. Three independent design passes (a thin-loop design, an adversarial anti-drift review, and a value and first-cases analysis) converged on this and disagreed on the following, resolved here:

- Fresh tree or prune v4: fresh minimal tree, `amp-fit`, no version number. In v4 the case was the tree itself, so repairing v4's own Markdown was sanctioned work, and every v4 pass did exactly that. A tree whose only cases are real repositories removes the trap structurally. v4's first-read chain was five negation-style files plus runnable lab bait and about 4,600 lines of spec-only documents; a third entry-path repair would have been the failure mode itself. Daniel authorized starting over.
- Skill length: at most 80 lines, no rule IDs, no tables. A long skill becomes a governance document the model treats as the job; v4's `METHOD.md` was 184 lines.
- A card file or the PR body: the PR body is the card. Cards are gradeable without an owner, so agents produce cards instead of work; the CAL card was 922 words of assumptions. A mergeable PR is the only artifact an owner actually grades. Empty and needs-decision passes end in the thread's final message with the same headings. No per-pass account files exist.
- Owner supplies the job or the agent infers it: the launch line carries `request=` when Daniel has one; otherwise the agent states its inferred responsibility first and proceeds, and `closed-wrong-job` catches misinference. Always supplying the job would never test discovery; always inferring would block on the owner's rescue.
- The metric: one ledger row per pass, five cells filled by Daniel (grade, correction category, his minutes, his estimate of minutes saved, one limitation phrase). Correction burden and value are both computed from those cells.
- Runtime: Orb via a personal Amp project per repository is primary, because it is the route that delivered PRs #27/#28 and the CAL run; local interactive Amp is the fallback.
- Distribution: the skill now. A plugin only when a graded row names a failure a plugin fixes (a needed `agent.end` continuation, an event trigger, a wrong mode).

## 10. The loop and the tree

`../README.md` is canonical and short. The tree holds seven files: `README.md`, `skills/amp-fit/SKILL.md`, `skills/amp-fit/ship.md`, `LEDGER.md`, this file, and two verbatim case records. Direct commits to main. The v4 repository is archived read-only with a pointer in its README; Amp_Fit_v3 is untouched.

## 11. First cases

Only Daniel's own repositories have a real owner who can grade. The OSS repositories used as apparatus have no consenting owner, and psf/requests' `AI_POLICY.md` forbids unsupervised agentic tools. SMASHED stays excluded unless Daniel names it.

| Order | Repository | Evidence of a real, recurring responsibility | Risk |
|---|---|---|---|
| 1 | `iamdanielkitchen/food-bridge-app` | Daniel already wrote the job in `MAINTENANCE-AGENT-PROMPT.md` ("KEEPER"): an audit routine, then a cleanup routine about an hour later; ledger compaction, PORTFOLIO residuals, `STATE.md` growth, stale docs; tiered authority (Tier A auto-fix on registered non-code surfaces, Tier B draft-and-queue); a frozen-artifact never-touch list; "several watched runs before scheduling"; "you never create scheduled tasks/cron yourself." Already an Amp project through the ampfit2-lab mirror. | The prompt is dated 2026-06-11 and names paths that may have moved; the Amp project binds a mirror, so the PR target is a decision; the frozen list makes wrong scope expensive, which is a good test of `missing-decision`. |
| 2 | `iamdanielkitchen/portfolio-site` | A manual render-verify loop (fourteen `fix(smashed)` commits on one day); `CONTACT-HARDENING-PLAN.md` says Phases 6–8 remain; `AJO-DEMO-HANDOFF.md` lists open items; local clone present. | No CI; verification is visual; the Orb HEAD differs from the dirty local tree; the site is password-gated. |
| 3 | `iamdanielkitchen/AJO` | CI `inquiry_engine` red on the latest runs; issue #10 "Factory Status" is a standing digest with no comments; draft PR #16. 5,403 files. | Idle since 2026-07-25, so an honest `empty-right` is possible; heavy context; better as a third case. |
| 4 | `iamdanielkitchen/interface_v0.1` | CI `suite` failing on its last five runs; small tree. | Idle seven weeks; likely superseded. |
| 5 | `iamdanielkitchen/ecomm-support-agent` (public) | The README claims an evaluation score; re-running the evaluation against current models is genuine recurring work. | Portfolio piece with no live demand. |

Decided 2026-09-19: the first case is `food-bridge-app`. The expected honest shape of a first pass is a Tier-A-only PR (hygiene on registered non-code surfaces, originals archived, frozen list untouched) with Tier B items queued under "What is unresolved," each naming Daniel as the decider. Case zero, before any new pass, is grading PRs #27 and #28; rows 1 and 2 of the ledger are pre-filled.

## 12. What would show the product exists

After two weeks (about ten passes, one owner, two or three repositories): at least two rows `merged` or `merged-after-fix` on two repositories; at most 30 % `closed-wrong-job`; at least one repeat pass on an accepted responsibility that built on the prior work rather than replaying it; the sum of `saved_min` on merged rows at least twice the sum of `daniel_min`. Two merges: continue, and let Daniel wire the first Automation on an accepted thread. Zero merges with mostly right selection: change the execution wording in the skill. Selection mostly wrong: change the assignment paragraph, not the packaging. Grading over fifteen minutes: change the PR body shape.

After six weeks (about thirty passes, two or three owners including one outside owner): at least eight merges; the outside owner at least two; at least three responsibilities with three or more repeat passes each; correction minutes falling on repeats; owner-estimated hours saved at least five against at most five hours of grading. Merges concentrated in one responsibility type means the product is that responsibility. Repeats regressing means continuity is the thing to fix. No outside merges after six outside passes means stop, or stay own-repo only.

The standing stop rules, with their numbers, live in `../README.md` so that changing a number is a one-line commit.

## 13. How this plan could die the same death

| Way it dies | Early sign | Rule that prevents it |
|---|---|---|
| `SKILL.md` grows into `METHOD.md` | a rule ID, a table, or a "read X first" pointer appears | 80-line cap; a line is added only citing a row graded `closed-wrong-job` |
| "Observed limitation" is satisfied by a document | any `plans/`, `later/`, `specs/` path; the word "limitation" outside a ledger cell | a limitation exists only as the `limitation` cell; software only when identical text appears in two graded rows, and then one file |
| The card becomes the deliverable | a pass ends in a Markdown account with no diff | no card files; the PR body is the account; no PR means `empty` and one sentence |
| Passes run where no owner grades | a PR older than 72 hours with a blank grade; a pass on a repo Daniel did not name | at most two ungraded rows at any time; blank after 7 days is `ungraded` and counts as not useful |
| The metric never gets a value | a sentence about what the metric should measure | the grade is a fixed enum Daniel types, plus integers; not revisable before row 10 |
| Document repair on the amp-fit tree substitutes for owner work | the target is an Amp Fit tree; the diff is Markdown only | the amp-fit tree is never the target; such a pass gets no row |
| The plan becomes the sixth apparatus | a forward plan longer than README plus SKILL, or describing anything past the next pass | README is at most 40 lines and ends with the launch command; once row 3 exists no planning document may be created |
| Launch waits on an authorization artifact or on transport work | an agent asks for a go-ahead file; a diff lands in transport code | Daniel's launch line is the authorization; transport failure means `blocked` and the local fallback, nothing else |

## 14. Open decisions for Daniel

- Give a `request=` line for pass 1 on food-bridge-app, or leave the job to inference (the KEEPER prompt is in the trail; inference is the real test).
- Create a personal Amp project for `iamdanielkitchen/food-bridge-app` so PRs land where he merges, or run the local interactive fallback.
- Grade PRs #27 and #28 today (case zero).
- After a first merge, whether to wire an Automation on that thread.
- Whether Amp's makers are an audience for the ledger (a fit or lead tool), a decision never recorded in any tree and not needed before the first outside owner.

## 15. Sources

- Trees: `/home/danielkitchen/Documents/Repos/amp-fit-v2` (499 commits, 2026-09-04 to 09-16); `/home/danielkitchen/Documents/Repos/Amp_Fit_v3` (66 commits, 09-12 to 09-16); `/home/danielkitchen/Documents/Repos/Amp_Fit_v4` (19 commits, 09-16 to 09-18); `/home/danielkitchen/Documents/Repos/SMASHED/docs/plans/2026-09-04-amp-repo-*.md`.
- v1 audit: `amp-fit-v2/PLAN.md` §2–3. v2 diagnosis: `amp-fit-v2/docs/recommendations/amp-fit-v3.md`; v2 lab: `amp-fit-v2/lab/out/cost_report.md`, `lab/out/capability.json`; v2 wrap: `amp-fit-v2/docs/recommendations/48h-wrap.md`.
- v3: `Amp_Fit_v3/CHARTER.md`, `LIMITATIONS.md`, `docs/amp-native-workflows/14-screen-two-experiment-results.md`, `16-preserved-proposal-review.md`, `24-automation-feasibility-v2.md`; AJO scan `~/amp-fit-v3-work/clones/ajo-scan-20260913T212036Z-22ee55/report.md`; auditor campaign `~/amp-fit-v3-work/auditor-campaign-20260914/scorecard.json`; PR experiment `~/amp-fit-v3-work/experiments/native-real-work-v2-20260914T150857Z/` (thread `T-01a0a078-4920-7151-b73f-e7df654347fe`); PRs `Pain-Point-Pipeline/amp-fit-v2#27`, `#28`.
- v4: `Amp_Fit_v4/METHOD.md`, `docs/workflow-selection-error.md`, `docs/cases/*.md`, `docs/history/initial_checkpoint.md`, `docs/plans/2026-09-18-0936-feat-production-work-foundation-plan.md`, `docs/later/`; runs `~/amp-fit-v4-work/automation-feasibility/cal-20260917T184938014818Z` (thread `T-01a0b0b3-fc4c-74aa-94f1-99e6d5e3655b`) and `rpath-20260917T190057220195Z` (thread `T-01a0b0be-5a62-73fd-8b5d-6512b0c13f7b`); review `~/amp-fit-v4-work/review-latest-20260917/review.md`; `amp threads usage` for the CAL thread ($0.08).
- Amp: installed CLI `0.0.1788279758-ge2ac2e` (`amp --help`, `amp skill list`, `amp plugins show-docs`); ampcode.com/docs/customize/skills, /docs/customize/plugins, /docs/cli/execute-mode, /docs/cli/spawning-orbs, /docs/cli/streaming-json, /docs/orbs/automations.
- First cases: `gh api` on `iamdanielkitchen/food-bridge-app` (`MAINTENANCE-AGENT-PROMPT.md`), `portfolio-site` (`CONTACT-HARDENING-PLAN.md`, `AJO-DEMO-HANDOFF.md`), `AJO`, `interface_v0.1`, `ecomm-support-agent`, all read on 2026-09-19.

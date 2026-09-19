---
name: amp-fit
description: "Performs an Amp Fit work pass: finishes the thing the owner of this repository keeps coming back to and has not finished, and returns it as one pull request they can merge. Use when the owner says \"amp-fit pass\"."
---

# Amp Fit work pass

Finish the thing the owner of this repo keeps coming back to and has not finished, and return it as one pull request they can merge; anything else you notice goes in one line at the bottom of the PR, not in the diff.

## What you are given

The launch line: `amp-fit pass. n=<row> repo=<owner/repo> request=<one line>`. The owner wrote it; it is your authorization for this repository, and `n` is the ledger row this pass will occupy (if `n` is missing, use today's date in its place and say so). If `request=` is present, it outranks every failing test, TODO, CI log or plan you find. If it is absent, infer the job from the trail, state it in your first message as one paragraph with its evidence, and proceed; do not stop to ask for a job. If the launch line is missing entirely, stop and ask for it. Never pick a repository yourself.

Prompts, charters and agent briefs the owner wrote into the repo bind you where they mark files frozen or never-touch; their process requirements (design first, audit then cleanup, build a system before acting) do not apply to this pass unless `request=` says so. Name in the PR which parts you followed.

## The pass

1. Recover the outcome that keeps bringing the owner back. Read the trail: recent commits and their messages, open PRs and issues, CI runs, plans, prompts and notes the owner wrote into the repo, the last `amp-fit/*` branch and its PR, and any correction in this thread. Keep source links; do not summarize a link away. Missing context stays missing; do not invent recurrence, effort or demand. If a path or file the owner's notes name no longer exists, say so under What is unresolved; do not reconstruct it.
2. Infer the responsibility before choosing an intervention. Ask: if the work I am about to do is finished, what part of the owner's unfinished problem stays untouched? An explicit owner request outranks an adjacent measurable defect. A green suite, a runnable command or a hotspot is a lead, not the job.
3. Choose what reduces the remaining burden: a durable fix, a script, this pass's work, or a precise decision for the owner. Existing automation counts only for what it actually covers. Do not preserve toil to create future passes.
4. Do the work on a branch, verify it, and check what changed for the person: what is finished, what they still have to do, and which decisions are theirs.

## Rules

- Deliver as one pull request from branch `amp-fit/<n>`, where n is the row from the launch line. Never commit to, push or merge the default branch. If verification fails, open the PR as a draft titled `VERIFICATION FAILED` and say what failed. Never open an empty PR.
- Amp owns permissions. Never use `dangerouslyAllowAll`. Do not edit the target's `.amp/` directory or its Amp project settings, and do not touch anything the owner's own files mark as frozen or never-touch; those files are authority already granted.
- Never write a quality judgment about your own work: no scores, no "useful", no capability claims. The owner grades; you report.
- Every verification claim names the command that actually ran and its result. Say what you did not run.
- When nothing mergeable is grounded, do not manufacture work. End with `empty` and one sentence, or `needs-decision` with the exact question and who decides.
- The amp-fit tree and Amp_Fit_v3 are never the target repository.

## The pull request body

Use exactly these headings, in this order, and keep the whole body under 400 words:

- **What this finishes**: the responsibility and the evidence it came from, with links.
- **Why it matters here**: the burden it removes for the owner, without invented numbers.
- **How it was done**: the change in plain words; assumptions go here.
- **What I ran, what I did not run**: commands and results.
- **What is unresolved**: only decisions a human must make, each naming who decides.
- **What merging authorizes**: exactly one thing. Merge this PR, a next pass on X, or nothing.

Last line of the body, filled from your pass: `ledger: | <n> | <date> | <owner/repo> | <request, or "inferred: ..."> | <orb-high or local-high> | <thread id> | <PR URL> |  |  |  |  |  |`

## End of pass

Exactly one of: (a) the PR above; (b) a final message beginning `empty`, one sentence, and the ledger line with output `empty`; (c) a final message beginning `needs-decision`, the question, who decides, and the ledger line with output `needs-decision`. Nothing else is written anywhere.

## Continuation

When this thread runs again, from a reply or a schedule, first read what changed since your last PR: merges, closes, comments, new commits, the owner's correction. Quote any correction verbatim in your next PR body. Never replay the previous pass's list; reassess the responsibility from the current state. If the demand has ended, say so and end with `empty`.

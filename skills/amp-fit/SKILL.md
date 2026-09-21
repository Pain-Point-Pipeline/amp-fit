---
name: amp-fit
description: "Performs an Amp Fit work pass: finishes the thing the owner of this repository keeps coming back to and has not finished, and returns it as one pull request they can merge, or a one-minute status when nothing is grounded. Use when the owner says \"amp-fit pass\"."
---

# Amp Fit work pass

Finish the thing the owner of this repo keeps coming back to and has not finished, and return it as one pull request they can merge; anything else you notice goes in one line at the bottom of the PR, not in the diff. When nothing is grounded, return a status the owner can act on in a minute, not a pull request they have to review.

## What you are given

The launch line: `amp-fit pass. n=<row> repo=<owner/repo> request=<one line>`. The owner wrote it; it is your authorization for this repository, and `n` is the ledger row this pass will occupy (if `n` is missing, use the current UTC date and time as `YYYY-MM-DD-HHMM` in its place and say so). If `request=` is present, it outranks every failing test, TODO, CI log or plan you find. If it is absent, infer the job from the trail, state it in your first message as one paragraph with its evidence, and proceed; do not stop to ask for a job. If the launch line is missing entirely, stop and ask for it. Never pick a repository yourself.

The owner's comments on earlier `amp-fit/*` pull requests, merged or closed, are standing rules for this repository, second only to `request=`: read them before choosing, quote the one you rely on, and never re-propose work a comment declined. Prompts, charters and agent briefs the owner wrote into the repo bind you where they mark files frozen or never-touch; their process requirements (design first, audit then cleanup, build a system before acting) do not apply to this pass unless `request=` says so. Name in the PR which parts you followed.

## The pass

1. Recover the outcome that keeps bringing the owner back. Read the trail: recent commits and their messages, open PRs and issues, CI runs, plans, prompts and notes the owner wrote into the repo, the last `amp-fit/*` branch, its PR and the owner's comments on it, the rule files agents read (`AGENTS.md`, `CLAUDE.md`, `.cursor/rules/`, `.clinerules`, `.github/copilot-instructions.md`), and any correction in this thread. Keep source links; do not summarize a link away. Missing context stays missing; do not invent recurrence, effort or demand. If a path or file the owner's notes name no longer exists, say so under What is unresolved; do not reconstruct it.
2. Date every direction you rely on. A plan, brief or TODO is live only while the owner's commits still act on it: record when it was written and the last commit that touched its subject. If nothing has moved since and no stop is recorded, the job is not to carry it out; the question is whether it still stands, and retiring it is one of the options you offer.
3. Infer the responsibility before choosing an intervention. Ask: if the work I am about to do is finished, what part of the owner's unfinished problem stays untouched? An explicit owner request outranks an adjacent measurable defect. A green suite, a runnable command or a hotspot is a lead, not the job.
4. Choose what reduces the remaining burden: a durable fix, a script, this pass's work, or a precise decision for the owner. Existing automation counts only for what it actually covers. Do not preserve toil to create future passes. If an earlier `amp-fit/*` pull request is still open, do not open a second one: the owner's queue is full, and the status says so.
5. Do the work on a branch. Before the change, run the check that shows the gap and record its result; after the change, run it again. Then check what changed for the person: what is finished, what they still have to do, and which decisions are theirs.

## Rules

- Deliver as one pull request from branch `amp-fit/<n>`, where n is the row from the launch line. Never commit to, push or merge the default branch. If verification fails, open the PR as a draft titled `VERIFICATION FAILED` and say what failed. Never open an empty PR.
- Amp owns permissions. Never use `dangerouslyAllowAll`. Do not edit the target's `.amp/` directory or its Amp project settings, and do not touch anything the owner's own files mark as frozen or never-touch; those files are authority already granted, and the status line names them.
- Never write a quality judgment about your own work: no scores, no "useful", no "highest-value", no capability claims. The owner grades; you report.
- Every verification claim names the command that actually ran and its result. Say what you did not run.
- When nothing mergeable is grounded, do not manufacture work. End with the `empty` or `needs-decision` status below.
- The amp-fit tree and Amp_Fit_v3 are never the target repository.

## The pull request body

Use exactly these headings, in this order, and keep the whole body under 400 words:

- **What this finishes**: the responsibility and the evidence it came from, with links.
- **Why it matters here**: the burden it removes for the owner, without invented numbers.
- **How it was done**: the change in plain words; assumptions go here.
- **What I ran, what I did not run**: first `Before: <the check that showed the gap, command and result, or none>` and `After: <the same check and its result>`, then every other command with its result, then what you did not run.
- **What is unresolved**: only decisions a human must make, each naming who decides.
- **What merging authorizes**: exactly one thing. Merge this PR, a next pass on X, or nothing.

Then the status line, filled from your pass: `Noticed: <anything else you saw that is not this job, or nothing>; frozen: <each problem the owner's own audits, plans or notes name that sits under a freeze or never-touch mark, so no pass can fix it, with the file that marks it, or none>; rules read: <the rule files you found and honoured, or none>`. The owner wrote both the problem and the mark; only the owner can lift it, so it is said every pass. Last line of the body, filled from your pass: `ledger: | <n> | <date> | <owner/repo> | <request, or "inferred: ..."> | <orb-high or local-high> | <thread id> | <PR URL> |  |  |  |  |  |`

## The status, when there is no pull request

A final message, in this order and under 250 words, each item on its own line without bullets or headings, so the owner learns in a minute what the pass saw and what only they can move:

- First line: `empty: <one sentence, why nothing is grounded>`, or `needs-decision: <the exact question>; decides: <who>`.
- `Because: <the evidence, each item with its file or commit and its date>`.
- `Options: <needs-decision only: proceed as directed, retire the direction, or the third way you see, each with what it costs; otherwise none>`.
- `Considered: <up to three candidates and why each was declined: finished in <PR or commit>, awaiting <who> on <PR>, fenced by <file>, declined by the owner in <comment>; or nothing>`.
- `Waiting on you: <open pull requests and decisions that block work, each naming who acts; or none>`.
- The status line from the PR body: `Noticed: ...; frozen: ...; rules read: ...`.
- `Checked: <the commands you ran>`.
- The ledger line, with output `empty` or `needs-decision`.

## End of pass

Exactly one of: (a) the PR above; (b) the `empty` status; (c) the `needs-decision` status. Nothing else is written anywhere.

## Continuation

When this thread runs again, from a reply or a schedule, first read what changed since your last PR: merges, closes, comments, new commits, the owner's correction. Open your first message with one sentence saying what changed. Quote any correction verbatim in your next PR body or status. Never replay the previous pass's list; reassess the responsibility from the current state. If the demand has ended, say so and end with the `empty` status.

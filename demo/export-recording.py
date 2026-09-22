"""Prepare the local portfolio replay from an Amp markdown export and the ledger.

Usage: python3 demo/export-recording.py thread.md verified-pr.json site/data/amp-fit.json
The input is the existing pass-13 thread. This does not launch work or publish.
"""
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from collections import Counter
from datetime import datetime, timezone


thread_path, result_path, destination = map(Path, sys.argv[1:])
result = json.loads(result_path.read_text())
if result.get("status") != "ready" or result["pr"].get("repo") != "iamdanielkitchen/portfolio-site":
    raise SystemExit("Expected a verified GitHub result for the recording's repository.")
pr = result["pr"]
root = Path(__file__).resolve().parent.parent
source = thread_path.read_text()
thread_id = "T-01a0bef2-e755-70db-81a9-b89a3b489c6a"
if f"threadId: {thread_id}" not in source:
    raise SystemExit("Expected the recorded pass-13 thread.")

blocks = re.split(r"^## (User|Assistant)\s*$", source, flags=re.M)
events = []
for index in range(1, len(blocks) - 1, 2):
    if blocks[index] != "Assistant":
        continue
    block = blocks[index + 1]
    # Preserve the source's prose. Omit its image attachment, which contains a
    # private signed asset URL; it is not needed to show the agent's activity.
    prose = block.split("**Tool Use:**")[0].strip()
    prose = re.sub(r"!\[[^\]]*\]\([^\n]+\)", "", prose).strip()
    if prose:
        # Paragraphs retain their exact wording and order, while each update
        # stays readable in the bounded activity surface.
        for paragraph in re.split(r"\n\s*\n", prose):
            events.append({"id": f"event-{len(events)+1}", "type": "message",
                           "text": paragraph, "sourceBlock": index})
    for match in re.finditer(r"\*\*Tool Use:\*\* `([^`]+)`\s*```json\s*(.*?)\s*```", block, re.S):
        payload = json.loads(match.group(2))
        command = payload.get("command", "")
        # Select the actual test invocation and commit/push commands. Do not
        # publish the raw export, file contents, tool results, or environment.
        if index in (51, 91) and match.group(1) == "shell_command":
            events.append({"id": f"event-{len(events)+1}", "type": "tool",
                           "tool": "shell_command", "text": command, "sourceBlock": index})

for event in events:
    if event["type"] == "message" and pr["url"] in event["text"]:
        event["result"] = "pull_request"
if not events or not any(event.get("result") for event in events):
    raise SystemExit("Recording does not contain the expected PR result.")

rows = []
for line in (root / "LEDGER.md").read_text().splitlines():
    cells = [cell.strip() for cell in line.split("|")[1:-1]]
    if len(cells) != 12 or not cells[0].isdigit():
        continue
    rows.append(dict(zip(("number", "date", "repo", "request", "runtime", "thread",
                          "output", "grade", "fix", "reviewMinutes", "savedMinutes", "limitation"), cells)))
for row in rows:
    for key in ("number", "reviewMinutes"):
        row[key] = int(row[key])
    row["savedMinutes"] = int(row["savedMinutes"]) if row["savedMinutes"] else None
graded = [row for row in rows if row["grade"] and row["grade"] != "void"]
merged = [row for row in graded if row["grade"] in ("merged", "merged-after-fix")]
commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
data = {
    "schemaVersion": 1,
    "generatedAt": datetime.now(timezone.utc).isoformat(),
    "recording": {"threadId": thread_id, "url": f"https://ampcode.com/threads/{thread_id}",
                  "date": "2026-09-20", "title": "Finish the SMASHED running loop",
                  "repo": "iamdanielkitchen/portfolio-site", "pass": 13,
                  "sourceSha256": hashlib.sha256(source.encode()).hexdigest(),
                  "timing": "compressed", "selection": "original assistant paragraphs and selected tool calls",
                  "events": events, "headBranch": pr["branch"],
                  "resultPath": "data/" + result_path.name},
    "evidence": {"source": f"https://github.com/Pain-Point-Pipeline/amp-fit/blob/{commit}/LEDGER.md",
                 "from": min(row["date"] for row in rows), "through": max(row["date"] for row in rows),
                 "passes": len(rows), "graded": len(graded), "merged": len(merged),
                 "repositories": len({row["repo"] for row in rows}),
                 "reviewMinutes": sum(row["reviewMinutes"] for row in rows),
                 "estimatedSavedMinutes": sum(row["savedMinutes"] or 0 for row in merged),
                 "outcomes": dict(Counter(row["grade"] for row in rows)), "rows": rows,
                 "baseline": None}
}
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
print(f"Exported {len(events)} recorded events and {len(rows)} ledger rows to {destination}")

# DetectionHammer AD Skill v1.1.0-rc.1

<p align="center">
  <img src="assets/detectionhammer-hero.svg" alt="DetectionHammer: Active Directory defensive validation, animated identity, telemetry and evidence layers" width="100%">
</p>


> **Repository staging notice:** The documentation is published; the complete release-candidate source tree has not yet been imported. The installation commands below become usable after the full source import. Native client and live SIEM testing remain outstanding.

Part 1: portable AI skill for authorized Active Directory defensive validation. Independent of DetectionHammer Hybrid v0.2 and its dashboard. English source files for AI-agent interoperability.

## Interactive product tour

Explore the animated 3D-style architecture, the 12 AD security domains and the synthetic evidence-verdict walkthrough in the [product tour source](docs/index.html). This is an illustrative website, not a live scanner or full catalog browser. To publish it, enable GitHub Pages for `main` → `/docs` in repository Settings → Pages.

## What is included
- 150 distinct AD defensive scenario cards in 12 modules (JSON, CSV and Markdown).
- ESC1–ESC16 posture review index, separate from the 150 count.
- 12 original experimental Sigma event visibility rules and 96 synthetic fixture cases.
- Offline Python catalog/fixture checker, evidence reporting workflow, integration guidance, and candidate ATT&CK mappings where applicable.
- Portable SKILL.md and optional Codex/Claude plugin manifests.

Not included: live attack executor, full 150-rule implementation, SIEM API connectors, deployment automation or live detection validation. The skill can review operator-supplied results from approved labs. No payloads or external command execution. Fixture checks are not tests of a real EDR/SIEM.

## Install as a skill (recommended)
Unzip. Copy the whole `skills/detectionhammer-ad` directory (including references, scripts and assets) into the project where you use your agent.

Claude Code (Linux/macOS/Git Bash):
```sh
mkdir -p .claude/skills
cp -R /path/to/extracted/skills/detectionhammer-ad .claude/skills/
```
Codex:
```sh
mkdir -p .agents/skills
cp -R /path/to/extracted/skills/detectionhammer-ad .agents/skills/
```
Windows PowerShell, from your project directory:
```powershell
New-Item -ItemType Directory -Force .claude/skills, .agents/skills | Out-Null
Copy-Item -Recurse /path/to/extracted/skills/detectionhammer-ad .claude/skills/
Copy-Item -Recurse /path/to/extracted/skills/detectionhammer-ad .agents/skills/
```
Replace `/path/to/extracted` with your extracted folder. Restart or refresh skill discovery if needed. Ask the agent to use `detectionhammer-ad` to review your authorized AD detection evidence. Availability varies by client and configuration. For ChatGPT, the included Codex-style plugin manifest is packaging scaffolding, not a published or installed ChatGPT plugin. If skill upload is unavailable, use the reference files as project context instead.

## Offline verification
From the extracted package root:
```sh
python skills/detectionhammer-ad/scripts/dh_review.py validate
python skills/detectionhammer-ad/scripts/dh_review.py fixtures
python skills/detectionhammer-ad/scripts/dh_review.py list --module KRB
python skills/detectionhammer-ad/scripts/dh_review.py show DH-KRB-001
```

Example request: “Use detectionhammer-ad to review my authorized AD lab's exported Wazuh events. Distinguish telemetry, alerts, and verified prevention; show evidence gaps and candidate defensive rule improvements.”

## Release limits
See TEST_RESULTS.txt for checks actually performed. Claude/Codex discovery and plugin loading have not been tested in their native clients. Sigma rule structure and equivalent fixture semantics were checked locally; no target SIEM compiler or live rule deployment was tested. Candidate ATT&CK mappings and log hypotheses need environment-specific analyst review. No claim of exhaustive coverage.

## Release candidate improvements

- Portable root Agent Plugins manifest plus local marketplace descriptors; compatibility manifests retained. Native installation still requires manual client testing.
- 12 expanded evidence cards (one per module); 138 remain baseline hypotheses. 34 mapping candidates have not been individually certified.
- 96 synthetic visibility cases, including missing and mistyped fields and legitimate administrative activity. Actual YAML is checked against the restricted watch-rule model in development tests; no Sigma backend compiler is claimed.
- Deterministic offline evidence-gate helper and synthetic example. It evaluates analyst assertions, not raw logs or verified execution. No output alone counts as live coverage.
- CI configuration, manual agent eval rubric, security/contribution policy and proposed MIT distribution license.

```sh
python -m pip install -r requirements-dev.txt
python -m unittest discover -s tests -v
python skills/detectionhammer-ad/scripts/evidence_verdict.py examples/evidence.json
```

Expected synthetic example verdict: `INCONCLUSIVE`. The alert search was not complete.

### Local plugin smoke tests (manual)

From the extracted package directory, Claude Code: `claude --plugin-dir .` and invoke `/detectionhammer-ad:detectionhammer-ad`. For Codex, use the standalone skill installation above or add the extracted directory as a local marketplace (`codex plugin marketplace add ./` where supported), then install the plugin from that source in the client. See `EVALS.md`. The marketplace files are static scaffolding, not certified installations or an official Plugins Directory listing.

No automatic usage tracking. Optional, voluntary public issues and sanitized feedback help guide development. DetectionHammer is independent of the planned ADhammer Enterprise product.

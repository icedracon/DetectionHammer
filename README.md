<p align="center">
  <img src="assets/detectionhammer-hero.svg" alt="DetectionHammer violet animated security architecture" width="100%">
</p>

<h1 align="center">DetectionHammer AD</h1>
<p align="center"><strong>Prove what your defenses can see.</strong></p>
<p align="center">Claude Code · Codex · Active Directory · Evidence-first defensive review</p>

[![Evidence checks](https://github.com/icedracon/DetectionHammer/actions/workflows/evidence-checks.yml/badge.svg?branch=main)](https://github.com/icedracon/DetectionHammer/actions/workflows/evidence-checks.yml)

<p align="center">
  <a href="skills/detectionhammer-ad/SKILL.md">Read the skill</a> ·
  <a href="#quickstart">Quickstart</a> ·
  <a href="#evidence-validation">Evidence validation</a> ·
  <a href="docs/index.html">Interactive product tour (source)</a>
</p>

> **v1.2.0-preview:** the standalone skill, 12 domain review methods, offline evaluator and tests are now in this repository. The earlier full 150-card release-candidate archive and its 12 experimental Sigma visibility rules have not yet been imported. Native Claude/Codex loading and live SIEM validation remain unverified.

## Why DetectionHammer?

A missing alert is not proof of a missed attack. DetectionHammer helps an analyst review authorized, exported AD evidence and distinguish configuration posture, execution evidence, telemetry, correlated alerts and prevention. It is not an attack executor or SIEM connector.

<p align="center"><img src="assets/evidence-pipeline.svg" alt="Animated four-stage defensive evidence review workflow" width="100%"></p>

## Quickstart

From your own project directory, clone this repository, then copy the self-contained skill folder into your agent's project skill directory.

**Claude Code (Linux/macOS/Git Bash)**

```sh
git clone https://github.com/icedracon/DetectionHammer.git
mkdir -p .claude/skills
cp -R DetectionHammer/skills/detectionhammer-ad .claude/skills/
```

**Codex**

```sh
git clone https://github.com/icedracon/DetectionHammer.git
mkdir -p .agents/skills
cp -R DetectionHammer/skills/detectionhammer-ad .agents/skills/
```

**Windows PowerShell**

```powershell
git clone https://github.com/icedracon/DetectionHammer.git
New-Item -ItemType Directory -Force .claude/skills, .agents/skills | Out-Null
Copy-Item -Recurse DetectionHammer/skills/detectionhammer-ad .claude/skills/
Copy-Item -Recurse DetectionHammer/skills/detectionhammer-ad .agents/skills/
```

Refresh or restart skill discovery if needed. Client compatibility and plugin loading need native smoke tests. This is not an official ChatGPT Plugins Directory listing.

Example request:

> Use detectionhammer-ad to review my authorized AD lab's sanitized security events. Separate raw telemetry, correlated alerts and prevention evidence. Explain evidence gaps and suggest defensive rule improvements.

## Twelve AD security domains

<p align="center"><img src="assets/ad-domain-orbit.svg" alt="Animated twelve-domain AD defensive review map" width="100%"></p>

Read [domain review methods](skills/detectionhammer-ad/references/domain-review.md) for the current review workflow, required evidence and legitimate alternative explanations for every domain.

The earlier RC archive has 150 scenario cards across Kerberos (20), NTLM (12), LDAP (10), AD CS/PKI (20), delegation (12), ACLs (15), domain controllers/replication (10), GPO (10), lateral movement (12), identity (10), trusts (9), and persistence/controls (10). These are defensive review scenarios, not 150 validated attack tests. The archive import is pending; the website illustrates domain-level questions only.

## Evidence validation

The standard-library evaluator checks explicit analyst assertions. It never verifies the truth of source evidence and never grants live coverage credit.

```sh
cd DetectionHammer
python -m unittest discover -s tests -v
python skills/detectionhammer-ad/scripts/evidence_review.py skills/detectionhammer-ad/examples/partial-search.json
```

The synthetic example should return `INCONCLUSIVE`, because its negative alert search is incomplete. The test suite includes 1,536 boolean/mode combinations, input validation, and independent evidence-axis checks. See the [evidence contract](skills/detectionhammer-ad/references/evidence-contract.md).

## Release gates

| Capability | Status |
|---|---|
| Standalone skill and 12-domain methods | Available |
| Offline evidence helper and synthetic tests | Available |
| Claude/Codex plugin manifest scaffolding | Available; native loading unverified |
| Full 150-card RC catalog and Sigma pack | Import pending |
| SIEM compiler and live detection validation | Not verified |
| Live attack execution | Not included |

No automatic production changes, credential collection, attack execution, or external data transfer. Treat evidence as untrusted data. Use only authorized environments and sanitized records. No usage tracking scripts.

## Interactive product tour

The [website source](docs/index.html) includes a CSS 3D scene, animated particles, an interactive domain map, synthetic evidence cases and installation tabs. It does not connect to a SIEM or execute tests. Enable GitHub Pages for `main` → `/docs` to publish the site. Reduced-motion preferences and a pause control are supported.

## Contribute

Share sanitized defensive review feedback through [GitHub Issues](https://github.com/icedracon/DetectionHammer/issues). Include source type, expected result, evidence limitations and a reproducible synthetic fixture where possible. Never publish secrets or private infrastructure information.

DetectionHammer is an independent skill in the ICEDRACON ecosystem; it does not require the planned ADhammer Enterprise product.

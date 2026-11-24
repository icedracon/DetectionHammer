# Development preview — beta release gates

Maintainer requested early beta testing before external validation is complete. The original stricter certification targets remain open; do not describe the beta as production-ready. The full source is imported into main for review. The official beta tag has not been created.

| Gate | Status |
|---|---|
| Complete source, catalog integrity, 150 draft methodologies | Local checks PASS; independent semantic review open |
| Evidence helper, synthetic fixtures | Local checks PASS; no live coverage |
| ATT&CK associations | 34 definition-level reviews; independent review open |
| Native Sigma backend / live SIEM | Not verified |
| Native Claude/Codex / npx skills | Not verified; manual file copy and relocated CLI pass |
| AI benchmark | 20 cases × 3 conditions; zero real trials |
| Cinematic visual | Included; public rendering not verified |
| License | Pending maintainer approval; LICENSE and manifest license declaration withheld |
| Public GitHub CI / tag / release | Full-project workflow configured; check GitHub Actions for actual result |

See TEST_RESULTS.txt for tests actually executed, EVALS.md for agent tests, SIGMA_VALIDATION.md for native conversion, and AUDIT.md for previous findings.

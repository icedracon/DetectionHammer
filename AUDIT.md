# DetectionHammer AD Skill: release candidate audit

Reviewed: original v1.0 archive, 2026-11-24. Proposed release: 1.1.0-rc.1.

## Findings and disposition

| Priority | Finding | Disposition |
|---|---|---|
| P0 | Catalog count could be confused with live execution or validated rules | README, skill and report explicitly separate posture, imported evidence, synthetic fixtures and native execution. |
| P0 | 100 evidence cards reused a generic evidence/control statement; 50 posture cards also reused a statement | Expanded 12 representative cards, one per module. Remaining 138 are baseline hypotheses, not expert-validated methods. |
| P0 | Original fixture checker only tested JSON representation | Development suite parses each actual YAML rule and checks its restricted event-watch logic against 96 synthetic cases. No target backend compilation. |
| P0 | No deterministic distinction between partial query and no alert | Offline verdict helper with strict boolean gates, incomplete-source handling, explicit evidence mode and no live coverage claim. Analyst assertions are not independently verified. |
| P1 | 34 candidate ATT&CK mappings are not individually audited | Preserve candidate status. Mapping review against current ATT&CK and vendor documentation remains open. |
| P1 | Plugin marketplace and portable manifest missing | Added root portable manifest, Claude and Codex compatibility manifests and marketplace descriptors. Native runtime and schema validation remain open. |
| P1 | No CI, license or contribution/security policy | Added offline CI, proposed MIT license and policies. CI itself has not run on GitHub. Maintainer should confirm license before publication. |
| P1 | No independent client evaluation or benchmark | Added 10 manual prompts and acceptance criteria. Neither client nor a live SIEM available here. |
| P2 | No user adoption measurement | Recommend voluntary feedback and GitHub traffic/release metrics, not silent telemetry. |

## Release recommendation

Ready for maintainer review and controlled public preview after license confirmation. Not ready to claim validated detection effectiveness or 150 executable tests. Before a stable release, verify both native client installations, conduct the manual eval rubric, audit scenario-specific methods and ATT&CK mappings, and test the rules on at least one target SIEM. Use redacted/synthetic data and record failures as well as successes.

## Scope and independence

Standalone skill and plugin package only. No ADhammer Enterprise source, attack runner, external connector, credentials, customer data or mandatory AI API is bundled. Local processing by scripts does not guarantee the AI client processes data locally. No automatic analytics are added.

## 0.0.1-dev.3 follow-up (local)

All 96 remaining baseline cards received individualized evidence requirements, negative controls and limitations. All 150 now have expanded draft methodology; this is an author review, not external certification. JSON/CSV/Markdown agreement is tested. The DC-006 and DC-007 titles were corrected to replica source naming-context establishment/removal because event 4928/4929 does not independently establish a connection-object change. LDAP-004 now includes the official LDAP channel binding documentation. Reference anchors: https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration and https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-channel-binding . The original audit table above is historical. The current status is in BETA_GATES.md.

Added offline AI benchmark score aggregation; incomplete/noncomparable runs cannot meet numerical release targets. The scorer cannot certify independence, truth of labels, or release readiness. No model trial was executed. No live attack executor or production deployment is included. Native Sigma/client/installer checks remain blocked or unexecuted.

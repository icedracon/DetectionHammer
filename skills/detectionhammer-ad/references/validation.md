# Evidence and validation protocol

## Scope record
Record environment, authorization owner, allowed host/identity scope, UTC time window, evidence provenance, source retention and query completeness. If authorization is uncertain, remain in offline review mode. Imported operator test evidence must carry a test/run ID, UTC time, host identity, declared test definition/version and independent execution record.

## Independent verdict axes
- Execution: confirmed / blocked-confirmed / failed / not-run / unknown.
- Telemetry: observed / no-match-in-complete-query / unavailable / partial.
- Alert: observed / no-match-in-complete-query / unavailable / partial.
- Posture: compliant / deviation / unknown / not-applicable, against an explicit policy.
- Fidelity: fixture-only / posture-review / imported-lab-evidence. Never equate these modes.

A genuine missed alert requires confirmed execution of an applicable scenario, an expected alert defined in advance, complete and healthy relevant sources, enough ingestion time, valid correlation, and no matching alert. Otherwise record inconclusive or not assessed. A blocked event needs direct prevention evidence. A normal event is not evidence of a malicious attack.

## Correlation
Normalize UTC times without discarding originals. Resolve immutable asset identities when available; account names and IPs alone are insufficient. Correlate on test ID when available, identity, host, provider, event record ID and bounded time. Record query provenance, source health, and conflicting evidence. Never invent event IDs or alerts. Store hashes of exported evidence only if actual bytes are available; hashes prove byte consistency, not truth.

## Report
For each scenario: ID, title, mode, mapping status, scope, observed evidence, source references, execution/telemetry/alert/posture axes, negative controls, confidence justification, alternative explanations, recommended defensive action and retest plan. Include unresolved prerequisites and unknowns. Report totals separately by mode. Coverage denominator includes only applicable executed scenarios with a defined expected outcome and sufficient evidence; show excluded and inconclusive counts. Report alert rate, prevention rate and raw visibility separately. Never count configuration reviews or offline fixtures as live detection coverage.

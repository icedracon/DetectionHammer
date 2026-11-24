# Detection rule engineering

The 150 catalog hypotheses are not 150 executable SIEM rules. The 12 bundled Sigma YAML rules are original experimental Windows Security event watch rules. The corresponding JSON is a deliberately restricted offline representation, not a general Sigma interpreter. They detect event visibility only.

Workflow: define the behavior and desired fidelity; confirm the provider, channel, audit policy, fields and normalized schema; establish approved administrative and service baselines; write a draft; test positive, negative and missing-field fixtures; validate with the target SIEM compiler or query parser; review historical false positives; have an analyst approve changes; retest and version the rule. No production deployment by this skill.

Do not use a generic EventID-only rule as proof of Kerberoasting, DCSync, ticket forgery, lateral movement or any other attack. Avoid universal thresholds and unverified field names. Aggregations and multi-source joins require backend-specific implementation and review. Use existing SigmaHQ rules only with their original license and attribution; no third-party rule files are redistributed here.

Sources: https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html and https://sigmahq.io/docs/basics/log-sources.html

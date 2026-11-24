# Domain and forest trusts

Sources: DC Security; trust inventory

Prerequisites: Collect Authentication Policy Change and authorized trust configuration snapshots.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-TRU-001 · Trust creation visibility
- Mode: evidence_review
- Candidate ATT&CK: T1484.002
- Mapping status: related_context_reviewed
- Candidate event IDs: 4706
- Method: Review new trusted domain relationship against approval
- Evidence: Compare the new trust record with approved architecture, counterpart ownership and change record.
- Negative control: Approved merger, migration or integration.
- Limitation: Trust existence does not demonstrate adversarial use.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1484/002/

## DH-TRU-002 · Trust removal visibility
- Mode: evidence_review
- Candidate ATT&CK: T1484.002
- Mapping status: related_context_reviewed
- Candidate event IDs: 4707
- Method: Review removed trust relationship against change record
- Evidence: Review the removed trust and approved decommission plan with dependent service owners.
- Negative control: Planned domain separation or retirement.
- Limitation: Removal is a related trust change, not necessarily adversarial trust manipulation.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1484/002/

## DH-TRU-003 · Trust modification visibility
- Mode: evidence_review
- Candidate ATT&CK: T1484.002
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4716
- Method: Review trust configuration changes against authorized baseline
- Evidence: Compare documented before/after trust configuration and approval with the scoped change record.
- Negative control: Approved changes during migration or maintenance.
- Limitation: Configuration drift alone does not establish misuse.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1484/002/

## DH-TRU-004 · Trust direction review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review trust relationships against business ownership
- Evidence: Compare trust direction and business owners with approved cross-domain access design.
- Negative control: Approved organizational integration or migration.
- Limitation: Trust direction alone does not establish effective cross-domain authorization.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-TRU-005 · Trust transitivity review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review transitive relationships against architecture requirements
- Evidence: Review transitivity settings against approved forest/domain architecture and documented exceptions.
- Negative control: Approved multi-domain design.
- Limitation: Configuration alone does not establish reachable resources or actual authentication.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-TRU-006 · Trust SID filtering posture
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review trust protections against approved security policy
- Evidence: Review approved trust configuration snapshots and security architecture decisions with domain owners.
- Negative control: Approved migration exception with documented expiry.
- Limitation: Settings alone do not establish cross-domain compromise.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-TRU-007 · Selective authentication posture
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review trust authentication controls against approved access design
- Evidence: Review effective selective-authentication posture against approved cross-domain access requirements.
- Negative control: Approved trust migration exception.
- Limitation: Configuration alone does not establish actual enforcement or resource access.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-TRU-008 · Cross-domain authentication anomaly
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4624, 4769
- Method: Review identity and destination domain context against authorized flows
- Evidence: Correlate source and destination domain identities in scoped authentication records against approved trust flows.
- Negative control: Approved cross-domain resource access.
- Limitation: Authentication records alone do not establish unauthorized cross-domain movement.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-TRU-009 · Trust inventory completeness
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review inventory coverage across in-scope domains and forests
- Evidence: Reconcile trust inventory across authorized domain owners and identify inaccessible or stale sources.
- Negative control: Approved retired domain or temporary inventory outage.
- Limitation: Partial inventory cannot establish that no additional trusts exist.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

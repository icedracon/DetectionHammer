# Delegation security

Sources: DC Security; directory inventory; identity sensor

Prerequisites: Collect directory change auditing and authorized delegation configuration snapshot.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-DEL-001 · Unconstrained delegation inventory
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review approved delegation inventory against tier boundaries
- Evidence: Review approved account inventory and documented delegation relationships with service owners.
- Negative control: Legacy service with a reviewed, time-limited exception.
- Limitation: Configuration posture alone does not establish delegation misuse.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-002 · Constrained delegation inventory
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review permitted service relationships against application ownership
- Evidence: Compare service relationship inventory with approved application dependency records and owners.
- Negative control: Approved service-to-service integration.
- Limitation: Configured relationship is not proof of actual use or exploitation.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-003 · Resource-based delegation inventory
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review authorized delegation principals and resource ownership
- Evidence: Review the authorized directory snapshot against approved service relationships and ownership.
- Negative control: Documented service provisioning and approved delegation.
- Limitation: Effective relationships require identity and permission context.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-004 · Delegation change on computer object
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Review computer object changes with delegation baseline
- Evidence: Scoped directory change record and before/after directory snapshot; compare changed property and object identity against approved change record.
- Negative control: Authorized delegation maintenance on a disposable lab object.
- Limitation: Directory change logging depends on SACL and audit policy; change alone is not compromise.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-005 · Delegation change on service identity
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Review service identity changes with change tickets
- Evidence: Compare service identity changes with before/after approved service configuration and change ticket.
- Negative control: Application deployment or service migration.
- Limitation: Object modification alone does not establish a delegated session.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-006 · Delegation change on privileged identity
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Review changes affecting privileged identity controls
- Evidence: Compare protected identity settings and ownership before/after the change with privileged-access approval.
- Negative control: Approved privileged account maintenance.
- Limitation: Change event does not establish subsequent privilege use.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-007 · Sensitive account delegation protection
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review protected identity settings against tier requirements
- Evidence: Review documented sensitive identities and effective delegation protection settings against approved tier policy.
- Negative control: Documented temporary application compatibility exception.
- Limitation: Configuration alone does not establish runtime enforcement.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-008 · Delegation service relationship drift
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Compare snapshots of approved service relationships
- Evidence: Compare dated service relationship inventories and reconcile changes with owner-approved dependency updates.
- Negative control: Approved migration or service retirement.
- Limitation: Snapshots may omit intermediate changes; drift is not evidence of exploitation.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-009 · Delegation principal lifecycle
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4726, 4743, 5136
- Method: Review identity deletion and delegation inventory consistency
- Evidence: Reconcile account removal events and remaining approved service relationships using stable object identities.
- Negative control: Normal decommissioning or service replacement.
- Limitation: Deletion records alone do not prove all related permissions were removed.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-010 · Delegated authentication anomalies
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4769
- Method: Review service authentication context with identity sensor evidence
- Evidence: Review existing identity-sensor alert and scoped service authentication records against known service relationships.
- Negative control: Routine approved delegated service operation.
- Limitation: Service-ticket telemetry alone cannot establish abusive delegation.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-011 · Delegation audit scope
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review SACL and collection coverage for critical objects
- Evidence: Review applicable SACLs, audit policy and collector source inventory for designated critical objects.
- Negative control: Approved audit scope exception or maintenance.
- Limitation: Configuration coverage is not event delivery or detection coverage.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DEL-012 · Delegation approval reconciliation
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review current delegation inventory against approved change records
- Evidence: Reconcile effective service relationship inventory with approved owner, ticket and review date.
- Negative control: Approved recently changed relationship awaiting inventory refresh.
- Limitation: A missing ticket may indicate documentation lag; not proof of abuse.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

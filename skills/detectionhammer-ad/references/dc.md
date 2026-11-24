# Domain controllers and replication

Sources: DC Security; Directory Service; EDR

Prerequisites: Collect DC audit logs and identity sensor findings; verify relevant SACLs.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-DC-001 · DCSync suspicion
- Mode: evidence_review
- Candidate ATT&CK: T1003.006
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4662
- Method: Review replication-related identity sensor alerts and audited directory access with approved replication inventory
- Evidence: Review identity sensor findings with directory access auditing, known replication roles and approved synchronization records.
- Negative control: Authorized domain replication and directory synchronization services.
- Limitation: A generic directory-access event is insufficient to demonstrate credential extraction.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1003/006/

## DH-DC-002 · Directory database access suspicion
- Mode: evidence_review
- Candidate ATT&CK: T1003.003
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4663
- Method: Review EDR findings and audited sensitive file access with backup context
- Evidence: Review authorized endpoint file-access evidence alongside backup inventory, process ownership and documented operations.
- Negative control: Domain controller backup, restoration or approved maintenance.
- Limitation: File-access events depend on audit policy and do not establish credential extraction.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1003/003/

## DH-DC-003 · Domain controller computer creation
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4741
- Method: Review new computer objects against approved DC lifecycle
- Evidence: Reconcile computer creation record with approved DC deployment inventory and subsequent role verification.
- Negative control: Approved server provisioning.
- Limitation: 4741 is a computer-account creation event, not proof the system became a DC.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DC-004 · Domain controller computer changes
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4742
- Method: Review computer account changes against approved maintenance
- Evidence: Compare computer account changes and DC maintenance record with authoritative role inventory.
- Negative control: Approved DC maintenance or machine account update.
- Limitation: 4742 alone does not establish a change in DC role or replication behavior.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DC-005 · Replication destination review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review authorized replication topology and endpoint ownership
- Evidence: Compare authorized replication topology and destination ownership with dated infrastructure inventory.
- Negative control: Approved DC addition or site migration.
- Limitation: Topology review is not proof of actual replication traffic or misuse.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DC-006 · Replica source naming context established
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4928
- Method: Review the audited replica source naming-context change against approved topology records
- Evidence: Reconcile replica source naming-context establishment with approved topology and maintenance records.
- Negative control: Normal DC promotion or topology convergence.
- Limitation: 4928 refers to a replica source naming context, not independently to a connection-object creation or malicious replication.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DC-007 · Replica source naming context removed
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4929
- Method: Review the audited replica source naming-context change against approved topology records
- Evidence: Reconcile replica source naming-context removal with approved topology and decommissioning records.
- Negative control: Normal topology adjustment or DC removal.
- Limitation: 4929 refers to a replica source naming context, not independently to a connection-object removal.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DC-008 · Directory backup governance
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review approved backup identities and access boundaries
- Evidence: Review backup identity inventory and approved access scope against documented recovery requirements.
- Negative control: Approved directory backup or restore service.
- Limitation: Role assignment alone does not establish backup contents or use.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DC-009 · DC privileged session activity
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4624, 4672
- Method: Review privileged sessions against dedicated admin workflows
- Evidence: Review DC destination logon and special-privilege records in the same host/session context against approved admin records.
- Negative control: Approved maintenance or service logon.
- Limitation: Special privileges assigned at logon do not prove they were exercised.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-DC-010 · DC audit source completeness
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review DC inventory, sensor health and log coverage
- Evidence: Compare the approved domain-controller inventory with each expected source heartbeat and retention record.
- Negative control: Documented maintenance outage and approved collector replacement.
- Limitation: Incomplete coverage makes negative detection claims inconclusive.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

# Group Policy security

Sources: DC Security; endpoint Security; SYSVOL audit

Prerequisites: Collect directory changes and relevant file share auditing; obtain authorized GPO snapshots.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-GPO-001 · GPO object creation
- Mode: evidence_review
- Candidate ATT&CK: T1484.001
- Mapping status: related_context_reviewed
- Candidate event IDs: 5137
- Method: Review newly created policy objects and approval records
- Evidence: Correlate the policy object creation record with its owner, scope and approved change ticket.
- Negative control: Creation of an approved new policy.
- Limitation: Object creation alone establishes neither policy application nor malicious modification.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1484/001/

## DH-GPO-002 · GPO object modification
- Mode: evidence_review
- Candidate ATT&CK: T1484.001
- Mapping status: concept_association_reviewed
- Candidate event IDs: 5136
- Method: Review policy metadata change and approved change request
- Evidence: Review before/after policy snapshots and the recorded change authorization for the same object.
- Negative control: Routine policy rollout or approved security hardening.
- Limitation: A directory update alone does not prove harmful policy effects.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1484/001/

## DH-GPO-003 · GPO object deletion
- Mode: evidence_review
- Candidate ATT&CK: T1484.001
- Mapping status: related_context_reviewed
- Candidate event IDs: 5141
- Method: Review deleted policy objects and change records
- Evidence: Review deleted policy identity, prior linked scope, approval record and restoration requirements.
- Negative control: Planned retirement of a superseded policy.
- Limitation: Deletion alone does not establish malicious activity or resulting host configuration.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1484/001/

## DH-GPO-004 · GPO link changes
- Mode: evidence_review
- Candidate ATT&CK: T1484.001
- Mapping status: related_context_reviewed
- Candidate event IDs: 5136
- Method: Review policy link changes and authorized scope
- Evidence: Compare approved link scope and before/after policy relationships with the corresponding change ticket.
- Negative control: OU reorganization and planned policy rollout.
- Limitation: Link change is a related policy action, not proof of harmful execution.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1484/001/

## DH-GPO-005 · GPO permissions review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review policy ACL and designated owners
- Evidence: Compare policy-object and associated file permissions against approved policy editors and owners.
- Negative control: Approved policy delegation.
- Limitation: Configuration review does not establish actual policy modification.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-GPO-006 · SYSVOL write audit
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5145
- Method: Review audited policy share access with file and change records
- Evidence: Review audited SYSVOL share access and independent file-change records against approved policy changes.
- Negative control: Normal policy deployment or administrative maintenance.
- Limitation: 5145 describes an access check; write-related access does not prove a completed file write.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-GPO-007 · GPO version consistency
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Compare approved policy versions across authorized snapshots
- Evidence: Review authorized policy backups and directory/SYSVOL version evidence with the change owner.
- Negative control: Expected propagation delay during an approved policy rollout.
- Limitation: Version mismatch alone cannot establish an attack.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-GPO-008 · Security policy drift
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review effective security baseline against approved policy
- Evidence: Compare effective security policy snapshot with approved baseline, scope and exception record.
- Negative control: Approved temporary compatibility policy.
- Limitation: Drift alone does not prove compromise or policy application across all hosts.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-GPO-009 · GPO script governance
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review centrally managed script inventory and approved owners
- Evidence: Review approved centrally managed script inventory and ownership against policy links and change records.
- Negative control: Approved software deployment or logon maintenance.
- Limitation: Inventory cannot establish script execution or integrity on every endpoint.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-GPO-010 · GPO audit completeness
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review directory and SYSVOL collection coverage
- Evidence: Reconcile directory and SYSVOL audit coverage with collector health and approved retention requirements.
- Negative control: Approved maintenance or forwarding exclusions.
- Limitation: One source cannot establish complete policy-change visibility.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

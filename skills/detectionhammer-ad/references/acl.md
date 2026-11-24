# Directory ACL and permissions

Sources: DC Security; authorized ACL snapshots

Prerequisites: Collect Directory Service Access and Changes; verify relevant SACLs.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-ACL-001 · Domain root ACL drift
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Review ACL changes with authoritative baseline
- Evidence: Domain root security descriptor snapshots from approved read-only exports; identify a material permission difference and reconcile with change records.
- Negative control: Approved permission maintenance with documented baseline and owner.
- Limitation: A changed descriptor is not proof that the permission was used.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-002 · Privileged group ACL drift
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Review group ACL changes against approved administrators
- Evidence: Compare privileged group security descriptors before and after the scoped directory change against approved role assignments.
- Negative control: Authorized delegated administration change.
- Limitation: General object change does not prove effective permission or group membership changed.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-003 · OU ACL drift
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Review organizational unit access changes with owner context
- Evidence: Review scoped OU permission snapshots and inheritance alongside change approval.
- Negative control: Approved organizational restructuring.
- Limitation: Inherited effects require separate evaluation; event alone does not prove access.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-004 · Service account ACL drift
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Review service identity ACL changes against ownership policy
- Evidence: Compare service account object permissions with ownership and application support role inventory.
- Negative control: Approved service owner transition.
- Limitation: Configuration change does not prove that the permission was exercised.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-005 · Computer object ACL drift
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Review computer object permission changes with owner context
- Evidence: Compare computer-object permissions and inheritance with approved device management roles.
- Negative control: Approved device enrollment or administrative transfer.
- Limitation: Object ACL change does not establish host-level compromise.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-006 · AdminSDHolder ACL review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review protected-object security descriptor baseline
- Evidence: Compare AdminSDHolder ACL snapshots and approved privileged-role design with directory change records.
- Negative control: Approved privileged administration model.
- Limitation: A snapshot alone cannot show runtime access or prove abuse.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-007 · Directory owner change
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136, 4670
- Method: Review available security descriptor changes and approved ownership records
- Evidence: Compare ownership records and security descriptor snapshots with approved ownership transfer; confirm event provider and object type.
- Negative control: Approved ownership recovery or administrative change.
- Limitation: 4670 may concern non-directory objects; require actual object context and appropriate source.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-008 · Inherited permission review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review effective permissions and inheritance with directory administrators
- Evidence: Review effective inherited permissions on scoped objects against parent policy and authorized role inventory.
- Negative control: Approved OU-level delegation.
- Limitation: Descriptor snapshot is not evidence of effective access for every identity without group context.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-009 · Replication permission review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review authorized replication-related permissions against approved services
- Evidence: Review effective directory replication permissions against the authorized replication and synchronization inventory.
- Negative control: Approved domain controllers and directory synchronization accounts.
- Limitation: Assigned rights do not prove that replication activity occurred.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-010 · Password reset delegation review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review delegated account management roles against support requirements
- Evidence: Review delegated account-support roles and approved reset permissions against organizational scope.
- Negative control: Approved help desk duties.
- Limitation: Permission existence is not evidence that any password was reset.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-011 · Group management delegation review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review authorized group management roles and owners
- Evidence: Compare group-management delegation and owner approvals with actual group scope and effective roles.
- Negative control: Approved group-owner delegation.
- Limitation: Rights inventory alone does not show that membership was changed.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-012 · GPO object ACL review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review policy object permissions against change governance
- Evidence: Review policy-object and associated file-side permissions against approved policy administration roles.
- Negative control: Approved policy management delegation.
- Limitation: Directory-side ACL alone is insufficient to evaluate the complete policy object.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-013 · Certificate template ACL review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review template security descriptors with PKI administrators
- Evidence: Compare certificate-template effective access and inheritance with approved PKI ownership and enrollment policy.
- Negative control: Authorized enrollment or template maintenance.
- Limitation: Template ACL posture is not proof of certificate issuance or misuse.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-014 · Unexpected directory access
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4662
- Method: Review audited access in context of object sensitivity and authorized actors
- Evidence: Review access event object identity and approved actor role alongside effective audit coverage.
- Negative control: Routine administrative read or inventory job.
- Limitation: Audit record alone does not establish sensitive data disclosure or malicious intent.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-ACL-015 · Directory SACL coverage
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review audit coverage for protected objects and sensitive changes
- Evidence: Compare protected-object SACL configuration and collection sources against defined audit requirements.
- Negative control: Approved targeted auditing to reduce noise.
- Limitation: A SACL snapshot cannot establish delivery, completeness or alert behavior.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

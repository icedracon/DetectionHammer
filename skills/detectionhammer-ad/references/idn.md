# Account and identity security

Sources: DC Security; identity inventory

Prerequisites: Collect Account Management and Logon auditing.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-IDN-001 · Domain account creation
- Mode: evidence_review
- Candidate ATT&CK: T1136.002
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4720
- Method: Review new identity against onboarding approval
- Evidence: Compare the account creation record with the identity provisioning request, creator and owner.
- Negative control: Approved onboarding and application-account provisioning.
- Limitation: Account creation does not establish unauthorized persistence.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1136/002/

## DH-IDN-002 · Domain account deletion
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4726
- Method: Review identity removal against offboarding records
- Evidence: Reconcile account deletion with stable account identity and approved offboarding ticket.
- Negative control: Normal employee offboarding or cleanup.
- Limitation: Deletion does not prove revocation of all sessions or external access.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-IDN-003 · Disabled account enablement
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4722
- Method: Review enablement against identity lifecycle approvals
- Evidence: Review account enablement actor and target with approved reactivation and owner record.
- Negative control: Approved returning employee or service recovery.
- Limitation: Enablement does not establish a subsequent sign-in.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-IDN-004 · Domain account disablement
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4725
- Method: Review disablement against approved lifecycle activity
- Evidence: Review disabled-account event with approved lifecycle action and owner confirmation.
- Negative control: Ordinary offboarding or temporary suspension.
- Limitation: Disablement alone does not prove all existing sessions ended immediately.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-IDN-005 · Password reset visibility
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4724
- Method: Review reset events with helpdesk and account owner records
- Evidence: Review reset-attempt outcome, target account and helpdesk authorization.
- Negative control: Approved account recovery or service maintenance.
- Limitation: 4724 can represent success or failure; reset attempt is not proof of account compromise.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-IDN-006 · Account lockout visibility
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4740
- Method: Review lockout records with authentication context
- Evidence: Review lockout record with scoped authentication timeline and support context.
- Negative control: Stale saved credentials or ordinary password errors.
- Limitation: Lockout alone does not establish hostile intent or the originating endpoint.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-IDN-007 · Privileged group member addition
- Mode: evidence_review
- Candidate ATT&CK: T1098.007
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4728, 4732, 4756
- Method: Review membership additions against access approvals
- Evidence: Compare membership change evidence and resulting membership snapshot with the privileged access request.
- Negative control: Approved just-in-time administration or role assignment.
- Limitation: A group addition does not establish attacker control; assess effective permissions separately.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1098/007/

## DH-IDN-008 · Privileged group member removal
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4729, 4733, 4757
- Method: Review membership removals against approved changes
- Evidence: Compare group membership removal record and approved role-change ticket using stable group and member identity.
- Negative control: Approved offboarding or access recertification.
- Limitation: Removal does not establish loss of all effective access through other memberships.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-IDN-009 · Account setting modification
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4738
- Method: Review user account changes against baseline and approval
- Evidence: Compare user account modification and relevant before/after attributes against approved lifecycle change.
- Negative control: Approved profile or policy maintenance.
- Limitation: A generic account change does not prove a security-sensitive setting changed.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-IDN-010 · Domain password policy review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review effective password policy against organizational requirements
- Evidence: Review effective password policy and applicable fine-grained policy inventory with approved identity governance.
- Negative control: Documented policy exceptions for managed identities.
- Limitation: A policy review is not proof of password strength or runtime enforcement.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

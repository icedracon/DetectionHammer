# Domain persistence and defensive controls

Sources: DC Security; EDR; directory inventory

Prerequisites: Collect directory and account management events; maintain protected-object baseline.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-PER-001 · Additional directory credentials review
- Mode: evidence_review
- Candidate ATT&CK: T1098
- Mapping status: related_context_reviewed
- Candidate event IDs: 5136
- Method: Review identity credential-related changes against approved provisioning
- Evidence: Review independently supplied directory attribute change records with credential governance and identity ownership.
- Negative control: Approved credential enrollment or rotation.
- Limitation: A generic directory change is not proof of unauthorized credential addition.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1098/

## DH-PER-002 · SID history change
- Mode: evidence_review
- Candidate ATT&CK: T1134.005
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4765, 4766
- Method: Review migration-related identity changes with approved migration records
- Evidence: Review SID-history change records alongside migration approval and independently supplied identity evidence.
- Negative control: Approved domain migration.
- Limitation: A change alone does not establish unauthorized token manipulation or use.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1134/005/

## DH-PER-003 · Privileged group persistence review
- Mode: evidence_review
- Candidate ATT&CK: T1098.007
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4728, 4732, 4756
- Method: Review persistent privileged access against periodic access review
- Evidence: Review privileged group changes, access approvals, expiry and resulting membership.
- Negative control: Approved temporary or permanent role assignment.
- Limitation: Membership change alone cannot demonstrate persistence or actor intent.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1098/007/

## DH-PER-004 · Protected identity permission drift
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review protected identity permissions against approved baseline
- Evidence: Compare protected identity effective permissions with dated approved baseline and owner review.
- Negative control: Approved privileged access recertification.
- Limitation: Permission drift does not prove persistence or actual access.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-PER-005 · Domain audit policy change
- Mode: evidence_review
- Candidate ATT&CK: T1685.001
- Mapping status: related_context_reviewed
- Candidate event IDs: 4719
- Method: Review changes to audit policy against approved maintenance
- Evidence: Compare audit policy snapshots and the authorized change record; assess whether logging was actually reduced.
- Negative control: Approved audit-policy tuning and maintenance.
- Limitation: A policy change event alone does not establish impaired logging.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1685/001/

## DH-PER-006 · Security log clear event
- Mode: evidence_review
- Candidate ATT&CK: T1685.005
- Mapping status: concept_association_reviewed
- Candidate event IDs: 1102
- Method: Review log clear evidence with administrator and retention records
- Evidence: Review the log-clear event with the responsible administrator, retention record and approved maintenance history.
- Negative control: Authorized log maintenance or lab reset.
- Limitation: The event establishes a reported clear action, not necessarily malicious intent.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1685/005/

## DH-PER-007 · Directory object restoration
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5138
- Method: Review restored object against recovery change records
- Evidence: Review directory object undelete record with stable object identity and recovery ticket.
- Negative control: Approved accidental-deletion recovery.
- Limitation: Restoration does not establish that all prior permissions or services were restored.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-PER-008 · Directory object move
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5139
- Method: Review moved object and policy scope impact against approval
- Evidence: Compare object-move record and before/after location with approved change and policy-scope review.
- Negative control: Approved OU restructuring.
- Limitation: An object move does not independently prove a resulting policy change or malicious persistence.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-PER-009 · Sensitive identity lifecycle drift
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review dormant, orphaned and unexpected privileged identities
- Evidence: Reconcile dormant and orphaned privileged identities with owner, employment/service status and approved exceptions.
- Negative control: Approved emergency or rarely used service account.
- Limitation: Inactivity and missing ownership records alone do not establish compromise.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-PER-010 · Defensive sensor coverage review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review endpoint and DC sensor health, coverage and retention
- Evidence: Compare expected endpoint sensors with the approved asset inventory, source heartbeat and retention status.
- Negative control: Documented maintenance or approved decommission.
- Limitation: Healthy heartbeat alone does not establish coverage for every security behavior.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

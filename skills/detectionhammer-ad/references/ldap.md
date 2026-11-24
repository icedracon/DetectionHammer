# LDAP security

Sources: Directory Service; DC Security; identity sensor

Prerequisites: Verify diagnostic logging and directory auditing where applicable.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-LDAP-001 · LDAP unsigned bind audit
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 2889
- Method: Review unsigned bind audit evidence and known legacy clients
- Evidence: Relevant DC Directory Service records identifying a client where the required diagnostic logging is enabled; verify client ownership and bind policy.
- Negative control: Approved signed or protected LDAP client sessions with an independently verified configuration.
- Limitation: Diagnostic logging is not necessarily enabled and event absence cannot establish secure binds.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-LDAP-002 · LDAP signing posture
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review effective DC LDAP signing policy
- Evidence: Review effective LDAP signing configuration from approved domain-controller inventory and change records.
- Negative control: Approved time-limited compatibility exception.
- Limitation: A snapshot does not prove all client connections are compliant.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-LDAP-003 · LDAP channel binding posture
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review effective channel binding policy and compatibility exceptions
- Evidence: Review effective channel-binding policy and documented client compatibility exceptions.
- Negative control: Approved temporary exception during migration.
- Limitation: Configuration is not evidence of runtime enforcement.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-LDAP-004 · LDAP channel binding warning
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 3039
- Method: Review channel binding audit diagnostics with client inventory
- Evidence: Review Directory Service channel diagnostics and effective channel-binding policy; reconcile affected client with owner.
- Negative control: Approved compatibility remediation in progress.
- Limitation: 3039 is policy and diagnostic dependent; absence is not assurance of successful enforcement.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/ldap-channel-binding

## DH-LDAP-005 · LDAP account discovery suspicion
- Mode: evidence_review
- Candidate ATT&CK: T1087.002
- Mapping status: concept_association_reviewed
- Candidate event IDs: 1644
- Method: Review directory query activity with diagnostic logging and approved administration baselines
- Evidence: Review directory diagnostic records with approved client inventory and the documented purpose of directory activity.
- Negative control: Identity inventory, address book synchronization and administration.
- Limitation: Event 1644 is selective diagnostic logging, not comprehensive directory query coverage.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1087/002/

## DH-LDAP-006 · LDAP group discovery suspicion
- Mode: evidence_review
- Candidate ATT&CK: T1069.002
- Mapping status: concept_association_reviewed
- Candidate event IDs: 1644
- Method: Review group query activity with legitimate application baselines
- Evidence: Compare directory diagnostic records about group lookup with known inventory jobs and client ownership.
- Negative control: Access reviews, authorization lookups and IAM synchronization.
- Limitation: A lookup alone is not hostile reconnaissance; absence may reflect diagnostic settings.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1069/002/

## DH-LDAP-007 · LDAP search performance audit
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 1644
- Method: Review expensive search diagnostics with application owners
- Evidence: Review directory search diagnostics with application owners and approved workload context.
- Negative control: Legitimate reporting or inventory application.
- Limitation: Diagnostic selection and thresholds affect visibility; expensive searches do not establish hostile activity.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-LDAP-008 · LDAP sensitive object access
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4662
- Method: Review audited object access with directory ownership records
- Evidence: Review audited object identity, access context and authorized role against the sensitive-object inventory.
- Negative control: Routine directory administration or access review.
- Limitation: Access auditing depends on audit policy and applicable SACL; record alone does not establish harmful use.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-LDAP-009 · LDAP directory change visibility
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Confirm object modification records reach collection pipeline
- Evidence: Compare a bounded authoritative object-change export with collector records and change ticket.
- Negative control: Approved directory maintenance.
- Limitation: A forwarded event does not establish complete directory-change coverage.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-LDAP-010 · LDAP diagnostic coverage
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review DC diagnostic level and collector availability without changing settings
- Evidence: Compare effective LDAP diagnostic configuration, channels and collector health against approved monitoring requirements.
- Negative control: Approved diagnostic reduction for resource management.
- Limitation: Configuration review cannot prove delivery or enforcement.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

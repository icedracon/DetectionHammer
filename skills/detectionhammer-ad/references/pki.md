# AD CS and certificate services

Sources: CA Security; DC Security; PKI inventory

Prerequisites: Enable Certification Services auditing and collect authorized CA inventory.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-PKI-001 · Certificate request visibility
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4886
- Method: Review request identity, template and CA records
- Evidence: Reconcile CA request records with request identity, issuance workflow and approved template inventory.
- Negative control: Ordinary certificate enrollment or renewal.
- Limitation: A request event does not establish issuance or subsequent certificate use.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-002 · Certificate issuance visibility
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4887
- Method: Correlate issuance with approved enrollment inventory
- Evidence: CA-issued certificate event correlated to request ID, approved template and certificate inventory; compare with the authorized enrollment record.
- Negative control: Routine approved certificate renewal and auto-enrollment.
- Limitation: Certificate issuance alone does not prove certificate misuse or authentication.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-003 · Certificate request denial
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4888
- Method: Review denied requests with enrollment support context
- Evidence: Review denied-request record and disposition against enrollment policy and support records.
- Negative control: Expired approval or ordinary enrollment failure.
- Limitation: Denial of one request does not prove all related requests were denied.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-004 · Certificate revocation activity
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4870
- Method: Review revocations against approved lifecycle actions
- Evidence: Reconcile revocation record with certificate inventory and lifecycle ticket.
- Negative control: Routine decommissioning or approved replacement.
- Limitation: Revocation event does not establish client-side revocation enforcement.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-005 · CA permission change
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4882
- Method: Review CA security changes with change approvals
- Evidence: Compare CA security changes with before/after access review and approved change ticket.
- Negative control: Authorized PKI role rotation.
- Limitation: Event presence does not establish effective permissions after inheritance or subsequent changes.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-006 · CA configuration change
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4890, 4891
- Method: Review CA configuration events with PKI administrator baseline
- Evidence: Compare CA configuration snapshot and audited change context to the approved maintenance record.
- Negative control: CA upgrade or approved property change.
- Limitation: 4890 and 4891 describe different configuration changes; inspect actual record rather than treating them as interchangeable.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-007 · Certificate manager settings change
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4890
- Method: Review certificate manager configuration with approval records
- Evidence: Compare certificate manager settings before and after the event with approved role policy.
- Negative control: Planned PKI responsibility reassignment.
- Limitation: Settings-change telemetry does not establish issuance or use of certificates.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-008 · Certificate template load visibility
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4898
- Method: Review template loading against CA inventory
- Evidence: Reconcile CA template-load record with approved CA template inventory.
- Negative control: Normal service startup or template refresh.
- Limitation: A loaded template does not establish its effective permissions or issuance.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-009 · Certificate template update visibility
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4899
- Method: Review template changes against change records
- Evidence: Compare template versions and approved change records with CA template-update observation.
- Negative control: Approved certificate policy rollout.
- Limitation: CA-side update observation does not establish complete directory-side change history.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-010 · Certificate template permissions update
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4900
- Method: Review template security change against approval and owner records
- Evidence: Review template security change evidence alongside authoritative security descriptor and owner approval.
- Negative control: Approved delegation change.
- Limitation: Effective permissions require separate review; an event alone does not establish misuse.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-011 · Enrollment permission review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review authorized template enrollment principals with PKI owners
- Evidence: Review authorized certificate template enrollment ACL inventory and owner-approved enrollment groups.
- Negative control: Documented enrollment role granted for a valid business requirement.
- Limitation: Effective rights depend on nested membership and CA/template settings.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates, https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-certification-services

## DH-PKI-012 · Template identity binding review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review certificate identity binding policy and template risk assessment
- Evidence: Review template identity-binding policy, approved certificate use and change history.
- Negative control: An approved purpose-specific identity enrollment workflow.
- Limitation: Template settings alone do not establish credential compromise.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates, https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-certification-services

## DH-PKI-013 · Template purpose review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review authentication-capable template purposes with business requirements
- Evidence: Compare template application purposes with approved certificate use cases and documented owners.
- Negative control: Authorized application-specific authentication template.
- Limitation: Purpose configuration alone does not establish exploitability or issuance.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-014 · Template approval review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review manager approval and issuance policy against requirements
- Evidence: Review effective approval requirements and documented exceptions for the scoped templates.
- Negative control: Approved unattended enrollment workflow.
- Limitation: Approval settings do not prove actual enforcement for every request.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-015 · Enrollment agent governance
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review enrollment agent permissions and restrictions with PKI owners
- Evidence: Reconcile authorized enrollment-agent roles and restrictions with documented certificate workflows.
- Negative control: Approved enrollment service performing its assigned role.
- Limitation: Inventory alone does not prove issuance controls are effective.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-016 · CA administrator governance
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review administrative role separation and access reviews
- Evidence: Compare CA administrator and certificate manager role inventory with separation-of-duties requirements.
- Negative control: Approved temporary break-glass assignment.
- Limitation: Role membership does not prove use or misuse of that role.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-017 · CA endpoint protection review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review enrollment endpoint authentication protections and transport policy
- Evidence: Review approved enrollment endpoint inventory and effective transport/authentication policy records.
- Negative control: Documented legacy endpoint migration exception.
- Limitation: A configuration snapshot is not proof of runtime enforcement or exploitability.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-018 · Certificate mapping policy review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review effective certificate mapping and strong binding posture
- Evidence: Review effective certificate mapping policy and documented compatibility exceptions against vendor guidance.
- Negative control: Approved certificate migration in progress.
- Limitation: Effective policy must be verified per relevant DC; configuration alone does not establish misuse.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

## DH-PKI-019 · Unusual certificate authentication
- Mode: evidence_review
- Candidate ATT&CK: T1649
- Mapping status: related_context_reviewed
- Candidate event IDs: 4768
- Method: Review certificate-backed authentication with CA and identity sensor evidence
- Evidence: Review certificate-related authentication evidence alongside CA issuance history, owner and approved certificate lifecycle.
- Negative control: Smart-card logon, normal renewal and certificate-based service authentication.
- Limitation: Unusual authentication does not establish certificate theft or forgery.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates, https://attack.mitre.org/techniques/T1649/, https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-certification-services

## DH-PKI-020 · PKI audit coverage
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review CA audit policy and collection completeness with known source inventory
- Evidence: Reconcile enabled CA audit categories and source inventory against approved collection requirements.
- Negative control: Scheduled collector outage or documented filtering.
- Limitation: Audit settings do not independently prove event completeness.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://learn.microsoft.com/en-us/defender-for-identity/security-posture-assessments/certificates

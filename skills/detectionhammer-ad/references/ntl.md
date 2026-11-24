# NTLM authentication

Sources: DC and endpoint Security; NTLM Operational

Prerequisites: Enable Credential Validation and Logon auditing; verify NTLM operational collection.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-NTL-001 · NTLM successful validation
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4776
- Method: Review approved legacy authentication baseline
- Evidence: Review successful credential validation status on the authoritative source and reconcile the account with approved legacy inventory.
- Negative control: Routine legacy application authentication.
- Limitation: Credential validation is not proof of a specific destination session.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-NTL-002 · NTLM failed validation
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4776
- Method: Review failure patterns with helpdesk context
- Evidence: Review failure status, reported workstation and account against support tickets and time window.
- Negative control: Expired service password or user typing error.
- Limitation: Failures alone do not establish malicious attempts or a subsequent success.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-NTL-003 · NTLM network logon
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4624
- Method: Review authentication package and source inventory
- Evidence: Confirm the authentication package and logon type in destination-host records; compare with approved client inventory.
- Negative control: Routine file-share or service access.
- Limitation: A network logon does not establish which business operation occurred.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-NTL-004 · Pass-the-hash suspicion
- Mode: evidence_review
- Candidate ATT&CK: T1550.002
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4624, 4776
- Method: Correlate endpoint and DC evidence with identity sensor findings; not proof of hash use
- Evidence: Correlate endpoint and identity alerts with scoped authentication records and independent incident evidence.
- Negative control: Approved legacy authentication and remote administration.
- Limitation: NTLM event presence cannot distinguish password-based logon from credential-material misuse.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1550/002/

## DH-NTL-005 · NTLM password spray suspicion
- Mode: evidence_review
- Candidate ATT&CK: T1110.003
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4625, 4776
- Method: Review account-distributed failures against known service disruptions
- Evidence: Review aggregate failed authentication records, scoped identity set, source health and service ownership.
- Negative control: Expired service credentials, misconfigured clients and legitimate user failures.
- Limitation: Authentication failures do not identify the attempted secret or prove a spraying campaign.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1110/003/

## DH-NTL-006 · NTLM privileged account use
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4624, 4776
- Method: Review privileged authentication against tier policy
- Evidence: Correlate privileged identity inventory with approved administration records and destination logon evidence.
- Negative control: Authorized legacy administration exception.
- Limitation: Validation events alone cannot establish privilege use at a destination.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-NTL-007 · NTLM service account use
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4624, 4776
- Method: Compare observed service identities with registered owners
- Evidence: Reconcile service account usage with documented application ownership and expected host relationships.
- Negative control: Scheduled batch job or application restart.
- Limitation: Shared service identity may limit attribution to a specific application.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-NTL-008 · NTLM workstation mismatch
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4624, 4776
- Method: Compare source identity and asset records with DHCP context
- Evidence: Resolve reported workstation and source-address context against time-valid inventory.
- Negative control: Renamed workstation, DHCP change or remote access gateway.
- Limitation: Reported workstation fields are not independent device identity proof.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-NTL-009 · NTLM audit policy review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review effective NTLM audit settings and coverage
- Evidence: Review effective NTLM auditing settings and a source-by-source collection inventory against the approved baseline.
- Negative control: Documented temporary policy exception.
- Limitation: Policy snapshots do not prove actual event delivery; check separate telemetry evidence.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-NTL-010 · NTLM restriction policy review
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review approved legacy exceptions and effective restriction settings
- Evidence: Compare effective NTLM restriction policies with the approved legacy-service register and exception owner.
- Negative control: Documented staged migration or temporary compatibility exception.
- Limitation: Configured policy does not establish enforcement on every host.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-NTL-011 · NTLM relay suspicion
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4624, 4776
- Method: Review identity sensor findings with server authentication context; events alone do not establish relay
- Evidence: Review the existing identity-sensor finding and corroborating server authentication evidence with the incident timeline.
- Negative control: Routine integrated authentication or approved proxy architecture.
- Limitation: Authentication records cannot independently establish relay; require qualified corroboration.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-NTL-012 · NTLM channel visibility
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review collector health and source availability for NTLM operational events
- Evidence: Compare NTLM operational channel availability and collector configuration across in-scope hosts.
- Negative control: Planned collector maintenance or approved channel filtering.
- Limitation: Configured collection does not prove end-to-end delivery.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

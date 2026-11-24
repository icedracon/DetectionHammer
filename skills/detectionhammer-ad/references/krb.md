# Kerberos security

Sources: DC Security; identity sensor

Prerequisites: Audit Kerberos Authentication Service and Service Ticket Operations; collect all relevant DCs.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-KRB-001 · Kerberoasting behavior
- Mode: evidence_review
- Candidate ATT&CK: T1558.003
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4769
- Method: Review service-ticket activity against account and service baseline
- Evidence: Compare DC ticket records with an independently recorded authorized test and established application usage.
- Negative control: Routine service authentication and scheduled jobs.
- Limitation: A ticket request alone does not establish password recovery or compromise.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1558/003/

## DH-KRB-002 · AS-REP roasting behavior
- Mode: evidence_review
- Candidate ATT&CK: T1558.004
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4768, 4771
- Method: Review unusual authentication requests and preauthentication status
- Evidence: Review successful authentication records with the account policy snapshot and independently documented lab activity.
- Negative control: Approved accounts with legacy authentication exceptions.
- Limitation: Failed preauthentication alone does not establish this technique; ticket acquisition does not establish password recovery.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1558/004/

## DH-KRB-003 · Golden ticket suspicion
- Mode: evidence_review
- Candidate ATT&CK: T1558.001
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4768, 4769, 4624
- Method: Correlate identity sensor alerts and ticket history; missing history alone is insufficient
- Evidence: Correlate identity alerts with historical DC and endpoint records and the independent incident or lab record.
- Negative control: Legitimate long-running sessions and incomplete retention.
- Limitation: Missing ticket history is not evidence of forgery.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1558/001/

## DH-KRB-004 · Silver ticket suspicion
- Mode: evidence_review
- Candidate ATT&CK: T1558.002
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4624, 4769
- Method: Review service-side logons and available KDC evidence; account for cached tickets
- Evidence: Review service-side authentication evidence alongside identity alerts and retained DC records for the scoped session.
- Negative control: Ordinary service sessions and cached credentials.
- Limitation: Missing DC events alone cannot establish ticket forgery.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1558/002/

## DH-KRB-005 · Pass-the-ticket suspicion
- Mode: evidence_review
- Candidate ATT&CK: T1550.003
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4624, 4769
- Method: Review unexpected account and device combinations with EDR context
- Evidence: Corroborate the scoped identity alert with session records and independently documented activity.
- Negative control: Approved service or administrator sessions.
- Limitation: Authentication records alone cannot establish ticket theft or reuse.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1550/003/

## DH-KRB-006 · Kerberos preauthentication failures
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4771
- Method: Review failures by account and approved client baseline
- Evidence: Group DC failure records by scoped account and time; compare reported client and failure reason with support records.
- Negative control: Expired cached credentials or user password errors.
- Limitation: Failures alone do not establish malicious intent or successful authentication.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-007 · TGT request anomalies
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4768
- Method: Compare account and source against historical authentication patterns
- Evidence: Compare observed TGT request identity, client and time with approved sign-in history and device inventory.
- Negative control: New workstation or scheduled service startup.
- Limitation: A new client is not evidence of account compromise; schema varies by DC update.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-008 · Service ticket failure anomalies
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4769
- Method: Review result codes and expected service activity
- Evidence: Review service-ticket failure status and service identity alongside outage or maintenance records.
- Negative control: Service rename, unavailable service or configuration error.
- Limitation: A failed request does not establish successful service access.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-009 · Ticket renewal anomalies
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4770
- Method: Compare renewal activity with account usage policy
- Evidence: Compare renewal timestamps and identity with documented service session lifetimes.
- Negative control: Long-running approved applications and ordinary renewals.
- Limitation: Renewal records do not establish ticket theft.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-010 · Legacy ticket encryption visibility
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4769
- Method: Review negotiated encryption with migration inventory
- Evidence: Compare recorded ticket encryption type with service inventory and approved migration exceptions.
- Negative control: Approved legacy application compatibility.
- Limitation: Ticket encryption is not necessarily the session-key encryption; verify event version.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-011 · TGT encryption policy visibility
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4768
- Method: Check ticket encryption fields against approved policy
- Evidence: Review TGT encryption fields from the actual event version against the effective authentication baseline.
- Negative control: Documented compatibility exceptions during migration.
- Limitation: Advertised or supported types do not establish which encryption was negotiated.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-012 · Service account ticket volume
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4769
- Method: Review service usage changes with owner context
- Evidence: Compare scoped service account ticket totals to its own business-hour and batch-job history.
- Negative control: Approved batch workload or deployment spike.
- Limitation: Volume alone is not proof of malicious activity; incomplete DC collection biases counts.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-013 · Privileged account Kerberos usage
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4768, 4769
- Method: Compare privileged identities with approved administration inventory
- Evidence: Reconcile privileged account authentication records with approved admin workstations and change windows.
- Negative control: Documented emergency maintenance or delegated administration.
- Limitation: Privilege membership and a ticket event do not prove privileged action.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-014 · Dormant identity Kerberos activity
- Mode: evidence_review
- Candidate ATT&CK: T1078.002
- Mapping status: related_context_reviewed
- Candidate event IDs: 4768, 4769
- Method: Correlate sign-in activity with identity lifecycle records
- Evidence: Join the authentication record to the identity owner, lifecycle status and approved access record.
- Negative control: Reactivated employee, maintenance or break-glass account.
- Limitation: Dormancy alone does not establish unauthorized use.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1078/002/

## DH-KRB-015 · Unexpected client authentication
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4768
- Method: Compare source identity with registered devices
- Evidence: Reconcile client address at event time with device inventory, DHCP and approved remote access.
- Negative control: DHCP reassignment or approved VPN client.
- Limitation: IP attribution can be ambiguous behind shared gateways.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-016 · Service principal change
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Review directory change audit against approved change tickets
- Evidence: Compare the audited SPN attribute change and object identity with before/after directory snapshots and owner approval.
- Negative control: Approved service migration or rename.
- Limitation: An object-change record alone does not establish subsequent ticket activity.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-017 · Preauthentication setting change
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4738, 5136
- Method: Review account configuration changes with approval evidence
- Evidence: Compare relevant account policy before and after the reported change with the documented exception and owner.
- Negative control: Approved legacy authentication exception.
- Limitation: A general user change event does not identify the precise setting without attributes or snapshots.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-018 · Kerberos delegation setting change
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 5136
- Method: Review delegation-related configuration changes against baseline
- Evidence: Compare audited service configuration attribute changes with approved delegation inventory.
- Negative control: Application onboarding or service migration.
- Limitation: The event establishes a configuration observation, not actual delegated authentication.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-019 · Kerberos event ingestion completeness
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4768, 4769, 4771
- Method: Compare collector records with authoritative DC event export
- Evidence: Compare equivalent bounded DC exports and collector records by source, record identifier and time after ingestion delay.
- Negative control: Collector maintenance or expected forwarding filters.
- Limitation: Incomplete retention prevents a reliable missing-event conclusion; event IDs alone do not identify unique records.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-KRB-020 · Kerberos policy baseline
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review effective ticket and encryption policies with administrator-provided snapshot
- Evidence: Review effective domain Kerberos policy and approved compatibility exceptions with the domain owner.
- Negative control: Documented compatibility setting with expiry and owner.
- Limitation: A policy snapshot is not a runtime authentication or detection test.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

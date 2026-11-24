# Domain lateral movement

Sources: Endpoint Security; Sysmon; EDR; network IDS

Prerequisites: Collect endpoint and server audit data; validate clocks and asset identities.

These are candidate detection hypotheses or posture reviews, not attack execution instructions. Event IDs require source and schema verification.

## DH-LAT-001 · RDP logon visibility
- Mode: evidence_review
- Candidate ATT&CK: T1021.001
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4624
- Method: Review remote interactive session and approved access inventory
- Evidence: Review destination session logs and approved remote-access records for the scoped account and host.
- Negative control: Help-desk or administrator RDP sessions.
- Limitation: A successful remote session alone does not prove lateral movement.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1021/001/

## DH-LAT-002 · SMB share access visibility
- Mode: evidence_review
- Candidate ATT&CK: T1021.002
- Mapping status: related_context_reviewed
- Candidate event IDs: 5140, 5145
- Method: Review share access and administrative context
- Evidence: Review share-access records with the destination, identity, share purpose and approved administrative activity.
- Negative control: File access, backups and centrally managed software distribution.
- Limitation: Ordinary SMB share activity is not necessarily remote administration or adversary movement.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1021/002/

## DH-LAT-003 · WinRM session visibility
- Mode: evidence_review
- Candidate ATT&CK: T1021.006
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4624
- Method: Correlate remote management operational logs and endpoint context
- Evidence: Corroborate authentication records with independently supplied WinRM operational or management records.
- Negative control: Approved remote management and configuration automation.
- Limitation: A generic network logon event does not establish use of WinRM.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1021/006/

## DH-LAT-004 · WMI remote management visibility
- Mode: evidence_review
- Candidate ATT&CK: T1047
- Mapping status: concept_association_reviewed
- Candidate event IDs: 4688
- Method: Review WMI operational evidence and authorized administration
- Evidence: Correlate endpoint and management records that identify the approved WMI operation and its owner.
- Negative control: Inventory, monitoring and enterprise management software.
- Limitation: Process creation alone does not establish WMI use or remote origin.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1047/

## DH-LAT-005 · Remote service installation visibility
- Mode: evidence_review
- Candidate ATT&CK: T1569.002
- Mapping status: related_context_reviewed
- Candidate event IDs: 4697
- Method: Review service installation records with software deployment approvals
- Evidence: Review service installation records with endpoint management history and the authorized change ticket.
- Negative control: Software deployment, monitoring agent installation or updates.
- Limitation: Installation evidence does not establish execution or remote origin.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1569/002/

## DH-LAT-006 · Remote scheduled task visibility
- Mode: evidence_review
- Candidate ATT&CK: T1053.005
- Mapping status: related_context_reviewed
- Candidate event IDs: 4698
- Method: Review task creation records with remote session context
- Evidence: Review scheduled task creation with the task owner, approved maintenance record and supplied runtime evidence if relevant.
- Negative control: Scheduled maintenance and centrally managed tasks.
- Limitation: Creation alone does not establish task execution or remote origin.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1053/005/

## DH-LAT-007 · Explicit credential logon visibility
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4648
- Method: Review explicit credential usage and authorized administration
- Evidence: Review explicit-credential logon record with process, session and approved administration context where available.
- Negative control: Approved run-as or scheduled administrative operation.
- Limitation: 4648 records an attempt with explicit credentials, not proof of successful remote logon.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-LAT-008 · Privileged network logon
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4624, 4672
- Method: Review linked logon and privilege events against administrative baseline
- Evidence: Correlate destination logon and special-privilege records in the same host/session context against management inventory.
- Negative control: Approved remote administration or service activity.
- Limitation: Privilege assignment does not establish a privileged operation or malicious movement.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-LAT-009 · Remote management source review
- Mode: evidence_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: 4624
- Method: Review source host identity against approved management systems
- Evidence: Reconcile destination logon source with approved management inventory and time-valid network context.
- Negative control: Approved support host or remote access gateway.
- Limitation: Source fields and gateway addresses may not uniquely identify the originating device.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-LAT-010 · Domain workstation session anomaly
- Mode: evidence_review
- Candidate ATT&CK: T1078.002
- Mapping status: related_context_reviewed
- Candidate event IDs: 4624
- Method: Review user/device deviations with identity context
- Evidence: Correlate the scoped session with account ownership, expected workstation use and incident context.
- Negative control: Travel, workstation replacement or approved support activity.
- Limitation: An anomalous session is not proof of compromised domain credentials.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration, https://attack.mitre.org/techniques/T1078/002/

## DH-LAT-011 · Lateral movement correlation completeness
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review endpoint, destination and DC source availability
- Evidence: Review whether endpoint, identity and network records share sufficient scope and time context.
- Negative control: Known collector outage or approved source migration.
- Limitation: Missing telemetry is a coverage limitation, not proof of prevention.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

## DH-LAT-012 · Administrative share governance
- Mode: configuration_review
- Candidate ATT&CK: None
- Mapping status: not_assigned
- Candidate event IDs: None (posture review)
- Method: Review approved remote administration and share access policy
- Evidence: Compare approved administrative share access policy and role inventory with documented support requirements.
- Negative control: Approved management and deployment services.
- Limitation: Share policy is not evidence of actual access or file transfer.
- References: https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration

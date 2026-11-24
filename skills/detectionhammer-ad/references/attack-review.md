# ATT&CK association review — 2026-11-24

Reviewed against the current public MITRE Enterprise technique definitions. A concept association is not an evaluated detection. A related-context association is weaker and must never receive technique coverage credit. Neither status proves an attack, rule quality, or applicability in a customer environment. Independent expert and telemetry review remain required.

| Scenario | Prior ID | Current ID | Association status | Evidence limitation | Source |
|---|---|---|---|---|---|
| DH-KRB-001 | T1558.003 | T1558.003 | concept_association_reviewed | A ticket request alone does not establish password recovery or compromise. | [MITRE](https://attack.mitre.org/techniques/T1558/003/) |
| DH-KRB-002 | T1558.004 | T1558.004 | concept_association_reviewed | Failed preauthentication alone does not establish this technique; ticket acquisition does not establish password recovery. | [MITRE](https://attack.mitre.org/techniques/T1558/004/) |
| DH-KRB-003 | T1558.001 | T1558.001 | concept_association_reviewed | Missing ticket history is not evidence of forgery. | [MITRE](https://attack.mitre.org/techniques/T1558/001/) |
| DH-KRB-004 | T1558.002 | T1558.002 | concept_association_reviewed | Missing DC events alone cannot establish ticket forgery. | [MITRE](https://attack.mitre.org/techniques/T1558/002/) |
| DH-KRB-005 | T1550.003 | T1550.003 | concept_association_reviewed | Authentication records alone cannot establish ticket theft or reuse. | [MITRE](https://attack.mitre.org/techniques/T1550/003/) |
| DH-KRB-014 | T1078.002 | T1078.002 | related_context_reviewed | Dormancy alone does not establish unauthorized use. | [MITRE](https://attack.mitre.org/techniques/T1078/002/) |
| DH-NTL-004 | T1550.002 | T1550.002 | concept_association_reviewed | NTLM event presence cannot distinguish password-based logon from credential-material misuse. | [MITRE](https://attack.mitre.org/techniques/T1550/002/) |
| DH-NTL-005 | T1110.003 | T1110.003 | concept_association_reviewed | Authentication failures do not identify the attempted secret or prove a spraying campaign. | [MITRE](https://attack.mitre.org/techniques/T1110/003/) |
| DH-LDAP-005 | T1087.002 | T1087.002 | concept_association_reviewed | Event 1644 is selective diagnostic logging, not comprehensive directory query coverage. | [MITRE](https://attack.mitre.org/techniques/T1087/002/) |
| DH-LDAP-006 | T1069.002 | T1069.002 | concept_association_reviewed | A lookup alone is not hostile reconnaissance; absence may reflect diagnostic settings. | [MITRE](https://attack.mitre.org/techniques/T1069/002/) |
| DH-PKI-019 | T1649 | T1649 | related_context_reviewed | Unusual authentication does not establish certificate theft or forgery. | [MITRE](https://attack.mitre.org/techniques/T1649/) |
| DH-DC-001 | T1003.006 | T1003.006 | concept_association_reviewed | A generic directory-access event is insufficient to demonstrate credential extraction. | [MITRE](https://attack.mitre.org/techniques/T1003/006/) |
| DH-DC-002 | T1003.003 | T1003.003 | concept_association_reviewed | File-access events depend on audit policy and do not establish credential extraction. | [MITRE](https://attack.mitre.org/techniques/T1003/003/) |
| DH-GPO-001 | T1484.001 | T1484.001 | related_context_reviewed | Object creation alone establishes neither policy application nor malicious modification. | [MITRE](https://attack.mitre.org/techniques/T1484/001/) |
| DH-GPO-002 | T1484.001 | T1484.001 | concept_association_reviewed | A directory update alone does not prove harmful policy effects. | [MITRE](https://attack.mitre.org/techniques/T1484/001/) |
| DH-GPO-003 | T1484.001 | T1484.001 | related_context_reviewed | Deletion alone does not establish malicious activity or resulting host configuration. | [MITRE](https://attack.mitre.org/techniques/T1484/001/) |
| DH-GPO-004 | T1484.001 | T1484.001 | related_context_reviewed | Link change is a related policy action, not proof of harmful execution. | [MITRE](https://attack.mitre.org/techniques/T1484/001/) |
| DH-LAT-001 | T1021.001 | T1021.001 | concept_association_reviewed | A successful remote session alone does not prove lateral movement. | [MITRE](https://attack.mitre.org/techniques/T1021/001/) |
| DH-LAT-002 | T1021.002 | T1021.002 | related_context_reviewed | Ordinary SMB share activity is not necessarily remote administration or adversary movement. | [MITRE](https://attack.mitre.org/techniques/T1021/002/) |
| DH-LAT-003 | T1021.006 | T1021.006 | concept_association_reviewed | A generic network logon event does not establish use of WinRM. | [MITRE](https://attack.mitre.org/techniques/T1021/006/) |
| DH-LAT-004 | T1047 | T1047 | concept_association_reviewed | Process creation alone does not establish WMI use or remote origin. | [MITRE](https://attack.mitre.org/techniques/T1047/) |
| DH-LAT-005 | T1569.002 | T1569.002 | related_context_reviewed | Installation evidence does not establish execution or remote origin. | [MITRE](https://attack.mitre.org/techniques/T1569/002/) |
| DH-LAT-006 | T1053.005 | T1053.005 | related_context_reviewed | Creation alone does not establish task execution or remote origin. | [MITRE](https://attack.mitre.org/techniques/T1053/005/) |
| DH-LAT-010 | T1078.002 | T1078.002 | related_context_reviewed | An anomalous session is not proof of compromised domain credentials. | [MITRE](https://attack.mitre.org/techniques/T1078/002/) |
| DH-IDN-001 | T1136.002 | T1136.002 | concept_association_reviewed | Account creation does not establish unauthorized persistence. | [MITRE](https://attack.mitre.org/techniques/T1136/002/) |
| DH-IDN-007 | T1098 | T1098.007 | concept_association_reviewed | A group addition does not establish attacker control; assess effective permissions separately. | [MITRE](https://attack.mitre.org/techniques/T1098/007/) |
| DH-TRU-001 | T1484.002 | T1484.002 | related_context_reviewed | Trust existence does not demonstrate adversarial use. | [MITRE](https://attack.mitre.org/techniques/T1484/002/) |
| DH-TRU-002 | T1484.002 | T1484.002 | related_context_reviewed | Removal is a related trust change, not necessarily adversarial trust manipulation. | [MITRE](https://attack.mitre.org/techniques/T1484/002/) |
| DH-TRU-003 | T1484.002 | T1484.002 | concept_association_reviewed | Configuration drift alone does not establish misuse. | [MITRE](https://attack.mitre.org/techniques/T1484/002/) |
| DH-PER-001 | T1098 | T1098 | related_context_reviewed | A generic directory change is not proof of unauthorized credential addition. | [MITRE](https://attack.mitre.org/techniques/T1098/) |
| DH-PER-002 | T1134.005 | T1134.005 | concept_association_reviewed | A change alone does not establish unauthorized token manipulation or use. | [MITRE](https://attack.mitre.org/techniques/T1134/005/) |
| DH-PER-003 | T1098 | T1098.007 | concept_association_reviewed | Membership change alone cannot demonstrate persistence or actor intent. | [MITRE](https://attack.mitre.org/techniques/T1098/007/) |
| DH-PER-005 | T1562.002 | T1685.001 | related_context_reviewed | A policy change event alone does not establish impaired logging. | [MITRE](https://attack.mitre.org/techniques/T1685/001/) |
| DH-PER-006 | T1070.001 | T1685.005 | concept_association_reviewed | The event establishes a reported clear action, not necessarily malicious intent. | [MITRE](https://attack.mitre.org/techniques/T1685/005/) |

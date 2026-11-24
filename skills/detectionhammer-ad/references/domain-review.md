# AD defensive review methods

These twelve domain guides are analyst review methods, not attack implementations or certified detections. Confirm event schemas and audit prerequisites against current Microsoft and vendor documentation. Only review approved environments and sanitized evidence.

| Domain | Review focus | Evidence to request | Legitimate alternatives / limitations |
|---|---|---|---|
| Kerberos | Authentication and service-ticket activity | DC authentication and ticket audit records, account context, identity sensor alerts | Scheduled application authentication and cached tickets; ticket events do not prove credential compromise |
| NTLM | Authentication posture and legacy dependencies | NTLM operational and authentication logs, host/application inventory, documented exceptions | Legacy applications and approved fallback; event presence does not establish abuse |
| LDAP | Signing, channel binding, directory access | Policy snapshots, directory service audit records, approved client inventory | Directory applications and routine inventory; availability depends on policy and audit settings |
| AD CS / PKI | Template permissions, enrollment and CA configuration | Authorized template/CA inventory, issuance and change audit records, certificate lifecycle policy | Normal auto-enrollment and renewals; posture issues are not proof of exploitation |
| Delegation | Service relationships and approved settings | Directory configuration snapshots, ownership, approved change records | Expected service-to-service relationships; review effective scope and business justification |
| ACL and permissions | Sensitive directory object access and changes | Effective-permission review, object owner, approved role assignments, change evidence | Authorized delegated administration; inherited permissions require context |
| Domain controllers and replication | DC health, replication role review and audit completeness | DC inventory, replication-role records, directory audit configuration and approved management activity | Legitimate directory synchronization and backups; review all relevant sources |
| Group Policy | Policy scope, configuration changes and ownership | GPO backups or snapshots, change records, linked scope and audit logs | Maintenance and policy rollout; change event alone is not malicious |
| Lateral movement | Remote administration visibility | Scoped endpoint, authentication and network records, approved administration inventory | Help desk, management agents and software deployment; corroborate endpoint and network evidence |
| Identity security | Account lifecycle, privilege assignment and authentication | Account management records, group membership snapshots and approved requests | Joiner/mover/leaver processes and planned role changes |
| Domain trusts | Trust inventory, ownership and changes | Trust configuration, approved design and audit records | Planned mergers or domain migration; do not infer cross-domain compromise from existence of a trust |
| Persistence and defensive controls | Security-sensitive configuration changes and restoration | Configuration baselines, audit records, maintenance tickets and rollback verification | Routine updates and authorized administration; evaluate context and source completeness |

## Analyst workflow for every domain

- Identify the control objective and the actual expected observation.
- Confirm source health, audit coverage, time window and permissions.
- Record source event IDs, alert IDs and independent activity evidence where applicable.
- Compare the finding with a relevant legitimate control and document uncertainty.
- For configuration findings, separate observed configuration from possible security consequences.
- Recommend a vendor-supported change or an approved review ticket; specify how to verify the outcome safely.
- For rule drafts, test positive and legitimate negative fixtures and the target SIEM field mapping before deployment. Generic event-ID matching is visibility, not proof of an attack.

Primary reference starting points:
- [Microsoft advanced security audit policy](https://learn.microsoft.com/windows-server/identity/ad-ds/plan/security-best-practices/advanced-audit-policy-configuration)
- [MITRE ATT&CK Enterprise](https://attack.mitre.org/matrices/enterprise/)
- [Sigma specification](https://sigmahq.io/sigma-specification/)

# Integration guidance (not implemented connectors)

Use only authorized read-only exports or an existing connector with explicit scope. This package makes no network requests. Confirm the exact product version and schema before suggesting native queries.

| Source | Evidence to request | Key caveat |
|---|---|---|
| Wazuh | Indexer raw/archive records if enabled, alert index, agent health | Manager API and Indexer are different; absent archive ingestion is not absence of activity |
| Elastic Security | Raw events and detection alerts separately | Verify index permissions, ECS mapping, partial results |
| Sentinel | SecurityEvent/WindowsEvent or actual workspace schema, alert/incident evidence | Workspace and connector determine table and field availability |
| Splunk | Authorized Windows events, CIM mappings, notable events when available | Confirm indexes and search completeness |
| Defender for Endpoint / Identity | Authorized sensor events, alerts, prevention action evidence | Verify licensing, sensor coverage and data retention |
| Kaspersky KATA/KEDR | Authorized alert/event export and prevention status if available | Product versions and export schema differ; no bundled connector or TAA syntax assumptions |
| Sysmon / Windows Event Log | EVTX or normalized event exports with provider, channel and host | Event IDs alone are ambiguous across providers |

Atomic Red Team: accept metadata and independently supplied results from approved lab exercises. Do not assume every ATT&CK technique has a faithful atomic test; distinguish test metadata, execution outcome and observed evidence. No Atomic Red Team commands, payloads or test libraries are bundled. Reference: https://github.com/redcanaryco/atomic-red-team

# Evidence contract

The offline helper accepts a JSON object with mode (synthetic, imported_lab_evidence, or posture_review), evidence_refs (unique nonempty strings), and nine explicit boolean assertions: authorized, execution_confirmed, expected_alert, sources_complete, ingestion_window_elapsed, correlation_verified, alert_observed, prevention_confirmed, telemetry_observed.

All claims are analyst assertions. The helper does not verify the evidence itself and always returns coverage_eligible=false. A prevention report and an alert report are independent and can coexist. Unauthorized inputs, missing references, absent execution proof, or incomplete negative searches never become a detection-gap claim. Configuration reviews are not runtime validation.

The three axes are execution, telemetry, and alert; prevention is a separate axis. Keep the evidence references in the local workspace. Avoid secrets or personal data in identifiers. A negative alert claim requires an expected alert, complete search, elapsed ingestion window and correlated execution. An observed alert must be correlated before it is reported as such.

Run with Python 3.9+ from the skill folder:
```text
python scripts/evidence_review.py examples/partial-search.json
```
The included example is synthetic and should produce INCONCLUSIVE. Never count fixture results as live EDR/SIEM validation.

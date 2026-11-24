#!/usr/bin/env python3
"""Offline evidence gate. Evaluates analyst assertions, never raw evidence."""
import argparse
import json
from pathlib import Path

GATES = ("authorized", "execution_confirmed", "expected_alert", "sources_complete",
         "ingestion_window_elapsed", "correlation_verified", "alert_observed",
         "prevention_confirmed", "telemetry_observed")
MODES = {"synthetic", "imported_lab_evidence", "posture_review"}

def evaluate(record):
    if not isinstance(record, dict):
        raise ValueError("Expected JSON object")
    if any(type(record.get(k)) is not bool for k in GATES):
        raise ValueError("All nine gates must be explicit booleans")
    if not isinstance(record.get("mode"), str) or record["mode"] not in MODES:
        raise ValueError("Invalid mode")
    refs = record.get("evidence_refs")
    if not isinstance(refs, list) or any(not isinstance(x, str) or not x.strip() for x in refs):
        raise ValueError("Expected nonempty string evidence references")
    if len(set(refs)) != len(refs):
        raise ValueError("Duplicate evidence references")
    r = record
    usable = r["authorized"] and bool(refs)
    correlated = usable and r["correlation_verified"]
    runtime = r["mode"] != "posture_review"
    execution = "REPORTED" if runtime and usable and r["execution_confirmed"] else "UNVERIFIED"
    telemetry = "REPORTED" if runtime and correlated and r["telemetry_observed"] else "UNVERIFIED"
    prevention = "REPORTED" if runtime and correlated and r["prevention_confirmed"] else "UNVERIFIED"
    alert = "UNKNOWN"
    if runtime and correlated:
        if r["alert_observed"]:
            alert = "REPORTED"
        elif r["execution_confirmed"] and r["sources_complete"] and r["ingestion_window_elapsed"]:
            alert = "NOT_REPORTED" if r["expected_alert"] else "NOT_EXPECTED"
    if not usable:
        verdict = "INCONCLUSIVE"
    elif not runtime:
        verdict = "NOT_RUNTIME_VALIDATION"
    elif prevention == "REPORTED":
        verdict = "PREVENTION_REPORTED"
    elif alert == "REPORTED" and execution == "REPORTED":
        verdict = "ALERT_REPORTED"
    elif alert == "NOT_REPORTED":
        verdict = "NO_ALERT_REPORTED_IN_COMPLETE_QUERY"
    elif alert == "NOT_EXPECTED":
        verdict = "NO_ALERT_EXPECTED"
    else:
        verdict = "INCONCLUSIVE"
    return {"mode": r["mode"], "verdict": verdict, "execution": execution,
            "telemetry": telemetry, "alert": alert, "prevention": prevention,
            "coverage_eligible": False, "evidence_verified_by_tool": False,
            "evidence_refs": refs if usable else [],
            "note": "Analyst assertions only; independently verify provenance."}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        if args.record.stat().st_size > 1_000_000:
            raise ValueError("Input exceeds 1 MB")
        record = json.loads(args.record.read_text(encoding="utf-8"))
        print(json.dumps(evaluate(record), indent=2))
    except (OSError, ValueError) as exc:
        parser.exit(2, f"Invalid evidence input: {exc}\n")

if __name__ == "__main__":
    main()

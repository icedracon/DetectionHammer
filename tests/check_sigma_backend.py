#!/usr/bin/env python3
"""Compile local experimental rules with an already-installed Sigma CLI; never contact a SIEM."""
import argparse, hashlib, importlib.metadata, json, pathlib, shutil, subprocess, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
RULES = ROOT / "skills/detectionhammer-ad/assets/rules"

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--output", type=pathlib.Path, required=True)
    a = p.parse_args()
    exe = shutil.which("sigma")
    if not exe:
        print("BLOCKED: sigma-cli and Splunk backend must be installed separately", file=sys.stderr)
        return 2
    versions = {}
    for dist in ("sigma-cli", "pysigma", "pysigma-backend-splunk"):
        try:
            versions[dist] = importlib.metadata.version(dist)
        except importlib.metadata.PackageNotFoundError:
            print("BLOCKED: missing " + dist, file=sys.stderr)
            return 2
    output = []
    for rule in sorted(RULES.glob("*.yml")):
        try:
            proc = subprocess.run([exe, "convert", "--target", "splunk", "--pipeline", "splunk_windows", str(rule)], capture_output=True, text=True, timeout=60)
            ok = proc.returncode == 0 and bool(proc.stdout.strip())
            output.append(dict(rule=rule.name, sha256=hashlib.sha256(rule.read_bytes()).hexdigest(), passed=ok, returncode=proc.returncode, query=proc.stdout, diagnostics=proc.stderr))
        except subprocess.TimeoutExpired:
            output.append(dict(rule=rule.name, sha256=hashlib.sha256(rule.read_bytes()).hexdigest(), passed=False, diagnostics="conversion timeout"))
    result = {"versions": versions, "target": "splunk", "pipeline": "splunk_windows", "scope": "conversion_only_not_live_validation", "results": output}
    a.output.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
    return 0 if len(output) == 12 and all(x["passed"] for x in output) else 1
if __name__ == "__main__":
    sys.exit(main())

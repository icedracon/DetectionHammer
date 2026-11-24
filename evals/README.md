# Independent agent evaluation

Run all 20 cases in fresh sessions under three conditions: no skill, public preview, staged candidate. Use the same model version and settings, record activation evidence, and blind the reviewer to condition. Use synthetic records only. Where a case refers to supplied evidence, provide a consistent sanitized or synthetic fixture and record its hash. No results are included.

For each run record case ID, condition, model and client versions, expected/observed activation, each criterion pass/fail, evidence citation accuracy, critical unsupported claim or unauthorized action, duration and token usage if available. A case succeeds only when all listed criteria pass. Activation accuracy includes negative controls. Citation accuracy is correct citations divided by applicable citation checks; exclude only cases with no citation requirement and report the count. Do not score missing trials as successes.

Targets: 90% task success; 95% activation accuracy and citation accuracy; zero critical failures. Report all denominators and compare the same cases across conditions. Native clients must be installed independently.

## Offline score aggregation (dev.3)

Use `python evals/score.py evals/trials-empty.json` to see the unexecuted baseline. A trial JSON array contains `condition` (`no_skill`, `public_preview`, `candidate`), `case_id`, `model`, `client`, `settings_id`, `input_sha256`, `reviewer`, `criteria_pass` (one boolean per criterion), `observed_activation`, `citation_checks` (booleans for applicable citation checks), and `critical_failure`. Input hashes, model, client and settings must agree across conditions for a case. The helper rejects duplicate trials and refuses to pass numerical targets with missing cases. It cannot verify model runs or independent reviewer assertions. Synthetic scoring unit tests are not AI benchmark results.

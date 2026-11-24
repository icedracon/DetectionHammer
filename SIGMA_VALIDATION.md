# Native Sigma conversion gate (not executed here)

The bundled 12 rules remain experimental event-visibility watches. Local tests exercise only the restricted EventID predicate and synthetic events. For native conversion, install `sigma-cli` and `pysigma-backend-splunk` in a clean development environment using reviewed versions. Then run:

```sh
python tests/check_sigma_backend.py --output sigma-conversion.json
```

The helper records installed package versions, file hashes, conversion output and errors. It does not deploy rules or query a SIEM. Independently validate representative positive and legitimate negative examples against the actual target schema before claiming detection support. Official instructions: https://sigmahq.io/docs/guide/getting-started and https://sigmahq.io/docs/digging-deeper/backends. This environment lacks the CLI and cannot resolve the package registry. No native conversion result is claimed.

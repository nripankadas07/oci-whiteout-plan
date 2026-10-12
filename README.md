# oci-whiteout-plan

Public alpha prepared on 12 October 2026. **Remote verification pending; not yet a verified launch.**
Original Python implementation, MIT, zero runtime dependencies. AI-assisted development.

Container build engineer reviewing captured layer entries. Explain why a lower-layer file disappears without extracting an untrusted image.

Compose normalized path manifests with ordinary and opaque OCI whiteouts, preserving same-layer additions and a deletion trace.

## Install and first useful result

Python 3.10+ (only Linux Python 3.12.14 tested in this preparation). Build requires setuptools 61+ and wheel already available; install into a fresh venv uses only the generated wheel. Run source tests with your build interpreter:

```sh
python -m pip wheel --no-index --no-deps --no-build-isolation --wheel-dir wheelhouse .
python -m venv .venv
.venv/bin/python -m pip install --no-index --no-deps wheelhouse/*.whl
.venv/bin/oci-whiteout-plan example.json
python -m unittest -v
```

The included synthetic input documents the exact normalized JSON schema.
Output is deterministic JSON; malformed inputs exit 2. Inputs are limited to 1 MiB.
No network connections, credential reads or writes to input files occur.
Hostnames, identifiers, paths and selected SSH values may be disclosed in output.
Review exported inputs and outputs before sharing. Use synthetic examples for reports.

## Scope and limits

Not an OCI runtime, tar extractor, image registry client, permission or link resolver.

Specific demand: Inferred; image-spec whiteout clarification and dive archive/path-safety reports are relevant evidence, not requests for this tool.
Discovery: Container-image diagnostics and OCI whiteout examples.
Portfolio distinction: No owned repository composes OCI whiteout manifests. portable-tree audits portability, not layer semantics.
See RESEARCH.md and the bundled research record for alternatives and incomplete research coverage.
No competitor absence, performance superiority or customer-adoption claim.

## Acceptance criteria

- Apply whiteouts only to lower-layer entries, regardless of member order.
- Reject traversal, absolute paths and unsupported entry kinds.
- Deterministic final paths and source-layer provenance.

## Support and contribution

Report a reproducible synthetic input, expected result, actual output and Python version.
Keep changes bounded and run the unit suite and clean installed example.
Do not submit private host configuration, production metric labels or credentials.
Security reports should omit secrets; this offline diagnostic is not a security boundary.
The source distribution is the supported install path; no registry release is claimed.

# Qualitative research — 12 October 2026

Observed 2026-10-12 06:35:23 UTC. Search queries: `container image analysis sort:stars-desc; OCI whiteout sort:stars-desc`.

GitHub search requested star ordering through query qualifiers. Direct repository-search REST fetch was unsupported; connector results were noisy and some irrelevant matches were rejected. Established adjacent tools were added explicitly, with current repository metadata, README and three recent open issue/PR records inspected. Ranking is the highest-star relevant comparable among these found sources, not an exhaustive global ranking. Code inspected for one relevant comparable in each area; complete competitor installations and full feature inventories were not tested.

| Repository | Stars | Last pushed UTC | API license |
| --- | ---: | --- | --- |
| [wagoodman/dive](https://github.com/wagoodman/dive) | 54634 | 2025-12-15T17:20:36Z | MIT |
| [google/go-containerregistry](https://github.com/google/go-containerregistry) | 4075 | 2026-10-07T20:50:50Z | Apache-2.0 |
| [opencontainers/umoci](https://github.com/opencontainers/umoci) | 964 | 2026-03-27T06:22:28Z | Apache-2.0 |

Highest-star relevant/adjacent source found in this inspected set: wagoodman/dive.

Dive explores image contents and efficiency; go-containerregistry supplies registry/image libraries and command-line tools; umoci unpacks and modifies OCI images. Those are broader image workflows. This candidate consumes a deliberately normalized path manifest, never extracts an archive, and emits lower-layer deletion reasons. It loses real image parsing, link handling, permissions and runtime fidelity. Existing tools are not claimed to lack an equivalent capability.

Installability, examples and support were assessed from current README/issue evidence. No measured time-to-result, reliability ranking, comparative speed or superiority claim is made. Our offline installed example passes; that establishes our behavior only. Specific demand remains inferred, as stated in README. All implementation code is original; no third-party source or prose was imported.

## Current evidence links

- wagoodman/dive: [README](https://github.com/wagoodman/dive/blob/main/README.md), observed blob `a97bdf42bcb3e9443fc8f2c3c49eea6f8877d1d9`.
  - [PR](https://github.com/wagoodman/dive/pull/725) — feat(config): support custom tui color theme configuration in .dive.yaml
  - [PR](https://github.com/wagoodman/dive/pull/724) — fix(docker): resolve blobs/sha256 layer paths in OCI archive images
  - [PR](https://github.com/wagoodman/dive/pull/723) — fix: contain extract paths to block tar-slip (CWE-22)
- google/go-containerregistry: [README](https://github.com/google/go-containerregistry/blob/main/README.md), observed blob `de70fb7c57349f3dfef0a9297304e4af615a7c15`.
  - [PR](https://github.com/google/go-containerregistry/pull/2467) — registry: verify manifest content matches digest reference on push
  - [PR](https://github.com/google/go-containerregistry/pull/2466) — fix(tarball): omit algorithm prefix from config filenames
  - [issue](https://github.com/google/go-containerregistry/issues/2464) — Upstream sync: manual merge needed (2026-10-05)
- opencontainers/umoci: [README](https://github.com/opencontainers/umoci/blob/main/README.md), observed blob `2d45012d77dae85b88faae069774d6df9a2394df`.
  - [PR](https://github.com/opencontainers/umoci/pull/679) — casext: error instead of panicking on a descriptor that overstates its size
  - [PR](https://github.com/opencontainers/umoci/pull/678) — config/convert: expose Config.Volumes as an annotation
  - [issue](https://github.com/opencontainers/umoci/issues/677) — Allow skipping of chowning rootfs dir when unpacking with rootless

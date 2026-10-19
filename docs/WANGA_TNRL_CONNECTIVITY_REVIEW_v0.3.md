# WANGA-TNRL Compiler-Processor — Connectivity Review v0.3

Date: 2026-10-19

## System identity
The target is a compiler that is itself a processor, not a conventional CPU hosting a compiler. A combined binary/ternary neural nano-processor fabric runs five programs together:
1. P1 — source collection and organization; preserve original order, context, and provenance.
2. P2 — structured compilation / Mishnah-like canonicalization.
3. P3 — interpretation.
4. P4 — rules of interpretation and compilation, including source-backed derivation methods.
5. P5 — derivation and adjudication, preserving competing outcomes and reasons.

The five programs are not five conventional CPU cores. They are the logical program set implemented by the combined binary/ternary fabric.

## Connectivity orders — preserve both
### C001 — previous order (preserved)
Source -> P1 collect -> P2 compile/canonicalize -> P3 interpret -> P4 apply interpretation/compilation rules -> P5 derive/adjudicate -> result.

### C002 — candidate order (test, not replacement)
Source capture with immutable IDs -> normalize into recursive Fractal IR while retaining the original source -> Formal Validator (schema, types, provenance, legal transitions) -> P2 canonical structure -> P3 interpretation branches -> P4 source-backed rule application -> P5 derivation/dispute evaluation -> output with alternatives, trace, digest.

C002 adds an explicit validation/provenance gate. Compare C001 and C002 on identical cases; do not accept C002 merely because it is more elaborate.

## Artifacts reviewed
- TNRL sandbox HTML source exists in ChatGPT Library; a live deployment URL is not verified.
- Nano-Node / Fractal IR report describes 21x21x21, ABA/IMMA sides, Receptoron/Phosphotron polarities, recursive IR, and validation.
- https://github.com/AmbassadorOv/multi-agent-orchestator/blob/main/README.md — baseline orchestrator with classifier, retrieval and reasoning agents; not equivalent to this compiler.
- https://github.com/AmbassadorOv/stunning-octo-garbanzo-d6cfaf53/blob/master/README.md — repository template, not proof of a complete runnable implementation.

## Sandbox constants
| Item | Value | Meaning |
|---|---:|---|
| Virtual topology | 21x21x21 | Grid per side and polarity |
| Sides | ABA, IMMA | Two logical sides |
| Polarities | RECEPTORON, PHOSPHOTRON | Two logical polarities |
| Total logical units | 37,044 | 21^3 x 2 x 2 |
| Active compute units | 36,000 | Total less reserved pool |
| Reserved control units | 1,044 | Functional allocation not yet documented |
| Operators | 21 | Signatures/contracts not yet formalized |

These are simulator design constants, not measured physical hardware results.

## Issues before benchmarking
1. HTML drawPipeline JavaScript appears to contain invalid/undefined identifiers or assignments; run it in a browser and record console errors.
2. HTML pulse behavior differs from Python tnrl_core.py, notably cross-polarity and mirror routing. Unify the execution contract before comparison.
3. Current Python P1-P5 transforms are numerical demonstrations, not actual Mishnah compilation, sourced interpretation, halakhic derivation, or adjudication.
4. The 1,044 control nodes are assigned by ID order without a documented functional partition.
5. Coordinate-based assignment to P1-P5 is provisional; define its architectural meaning.
6. Define all 21 operators' input types, preconditions, output types, errors, and provenance requirements.
7. Add source-backed golden cases with expected intermediate derivations and outcomes.
8. No live deployment URL has been confirmed; a saved HTML file is not a deployed site.
9. WANGA integration and Chrome Canary/CDP inspection are planned, not verified.
10. No controlled benchmark against an existing neural model or multi-agent orchestrator has been demonstrated.

## Implementation order
1. Freeze C001 and create separate C002 configuration.
2. Fix HTML syntax/runtime issues and test browser console.
3. Define a shared trace schema and make Python/HTML deterministic and equivalent.
4. Formalize recursive Fractal IR JSON Schema and the 21 operator contracts.
5. Implement source-preserving P1 and deterministic P2 before interpretation.
6. Implement P3-P5 with explicit source/rule references and branch-preserving adjudication.
7. Add unit, property, regression, and golden-corpus tests.
8. Benchmark C001 vs C002 and compare with a conventional LLM and multi-agent baseline using identical tasks and scoring.
9. Integrate WANGA after sandbox parity and validation pass.
10. Publish a versioned context seed every 3-4 substantial milestones; never overwrite old seeds.

## Benchmark metrics
Source retention rate; IR validation pass rate; rule-trace completeness; derivation reproducibility; adjudication agreement on gold cases; unsupported-claim rate; latency; memory; active nodes; trace events; baseline task accuracy.

## Versioning rule
Keep context_seed_v0.2.json unchanged. The v0.3 seed and this review are additive. Each configuration needs a unique ID, parent ID, source references, order, context, changes, known issues, and evaluation results. Do not label simulation as physical hardware or claim scientific validation without measurements.

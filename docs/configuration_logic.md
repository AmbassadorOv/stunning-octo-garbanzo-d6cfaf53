# RPHACH-72 Configuration Logic

## Verified structural finding

The 288 count is not best modeled as a single generic multiplication rule.

### Path A — four 72 blocks
Etz Chaim describes the 288 sparks as four 72-count aspects arising from the four YHVH expansions: AB, SAG, MA, BN. Crucially, the four contributions are **not numerically identical internally**: the text describes different counting rules for each name, while each contribution is classified as an AB-equivalent count. Therefore the engine stores both the aggregate 72 and the internal construction rule.

### Path B — 72 + 216
A separate documented representation decomposes 288 as 72 words plus 216 letters. This is a different input space and operation. It must not be merged with Path A merely because the output is 288.

### Path C — orientation
Etz Chaim also distinguishes face/back orientation in the four-part accounting: the first three AB aspects are treated as panim and the fourth as achor in the cited passage. This is stored as a configuration dimension, not as a universal rule for every source.

## Engine principle

Every configuration is represented as:

source -> input space -> operation -> ordering -> orientation -> output -> structural signature

Comparison classes:

- NUMERIC_MATCH_SOURCE_DISTINCT
- SAME_COUNT_DIFFERENT_CONFIGURATION
- SAME_CONFIGURATION_CANDIDATE
- NUMERIC_DIFFERENT

A numerical match is therefore evidence of equal cardinality, not proof of historical or structural identity.

## Related axes

- 22 Hebrew letters
- C(22,2) = 231 unordered pairs
- 22*21 = 462 ordered pairs without repetition
- 230 crystallographic space groups: computational symmetry comparison layer only
- 360: cyclic/time axis
- C(9,4) = 126: mathematical combinatorial axis, pending source attribution
- 36: reserved until its exact source/definition is fixed

## Crystallographic layer

The 230 space-group layer should be used as a **symmetry-analysis comparator**, not as a claim that Kabbalistic texts historically encode crystallographic space groups.

The future implementation should compare canonical signatures:

1. cardinality
2. partition structure
3. ordering/permutation
4. orientation
5. operation type
6. orbit/fixed-point pattern
7. source provenance

Only after these are separated should isomorphism or equivalence be tested.

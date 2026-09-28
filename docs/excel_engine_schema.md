# Spreadsheet / Excel Engine Schema

Use data/configuration_matrix.csv as the seed table.

Recommended columns:

| column | purpose |
|---|---|
| config_id | unique configuration |
| source_id | textual source |
| input_space | letters / words / names / calendar |
| input_count | number of input elements |
| operation | add / multiply / permutation / pairing |
| ordering | ordered / unordered |
| orientation | panim / achor / mixed / unknown |
| output_count | produced count |
| crystal_group_id | optional 1..230 |
| symmetry_signature | computed signature |
| letter_signature | letter-combination signature |
| equivalence_class | engine result |
| provenance_status | documented / inferred / unresolved |

## Core formulas

Unordered pairs of 22 letters:

=COMBIN(22,2)

Ordered pairs without repetition:

=22*21

Four AB blocks:

=4*72

Word/letter path:

=72+216

## Important rule

Do not put all formulas into one equivalence class merely because the output equals 288.

The spreadsheet should calculate three independent comparisons:

1. Numeric equality.
2. Operation equality.
3. Structural/signature equality.

Only when all required signatures agree should the result be marked STRUCTURAL_MATCH.

## Crystallographic experiment

For each of the 231 unordered letter pairs, assign a deterministic pair signature. Then test that signature against candidate symmetry signatures for the 230 crystallographic space groups.

This is an experimental computational mapping, not a historical identification of Hebrew letter pairs with crystallographic groups.

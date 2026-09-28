from dataclasses import dataclass, asdict
from math import comb, gcd
from typing import Any, Dict, List, Tuple

@dataclass(frozen=True)
class PathResult:
    config_id: str
    operation: str
    inputs: Tuple[str, ...]
    output: int
    tags: Tuple[str, ...]
    provenance: str
    orientation: str = "unspecified"
    ordering: str = "unspecified"

class RphachEngine:
    """Provenance-aware engine for 288/72 and related combinatorial paths.

    Numeric equality is not treated as structural equality.
    """

    def __init__(self, crystal_space_groups: int = 230):
        self.crystal_space_groups = crystal_space_groups

    @staticmethod
    def base_counts() -> Dict[str, int]:
        return {
            "letters": 22,
            "unordered_pairs": comb(22, 2),
            "ordered_pairs_no_repetition": 22 * 21,
            "ab": 72,
            "rphach": 288,
            "cycle": 360,
            "crystal_space_groups": 230,
            "c126": comb(9, 4),
        }

    @staticmethod
    def rphach_by_four_ab() -> PathResult:
        return PathResult(
            "C1", "4*72", ("AB", "SAG", "MA", "BAN"), 288,
            ("numeric_match", "four_blocks", "documented"),
            "Etz Chaim / Chabadpedia: four YHVH fillings/levels",
            orientation="source-specific",
            ordering="four_name_blocks",
        )

    @staticmethod
    def rphach_by_words_letters() -> PathResult:
        return PathResult(
            "C2", "72+216", ("72_words", "216_letters"), 288,
            ("numeric_match", "word_letter_decomposition", "documented"),
            "Documented alternative decomposition; keep source provenance separate",
            orientation="unspecified",
            ordering="words_then_letters",
        )

    @staticmethod
    def rphach_by_four_yhvhs() -> PathResult:
        return PathResult(
            "C3", "4*72", ("AB", "SAG", "MA", "BAN"), 288,
            ("structural_match_candidate", "four_yhvhs", "documented"),
            "Etz Chaim Sha'ar XVIII: distinct contribution rules for each name",
            orientation="source-specific",
            ordering="AB,SAG,MA,BAN",
        )

    @staticmethod
    def orientation_variant() -> PathResult:
        return PathResult(
            "C4", "4*72", ("three_panim", "one_achor"), 288,
            ("orientation_sensitive", "documented"),
            "Etz Chaim Sha'ar XVIII, chapter IV: first three aspects are panim; fourth is achor",
            orientation="panim-achor",
            ordering="three_plus_one",
        )

    @staticmethod
    def pair_spaces() -> Dict[str, int]:
        return {
            "unordered_231": comb(22, 2),
            "ordered_462": 22 * 21,
        }

    @staticmethod
    def modular_profile(values: List[int], modulus: int) -> Dict[str, Any]:
        return {
            "modulus": modulus,
            "remainders": {str(v): v % modulus for v in values},
            "gcd_with_modulus": {str(v): gcd(v, modulus) for v in values},
        }

    @staticmethod
    def classify(a: PathResult, b: PathResult) -> str:
        if a.output != b.output:
            return "NUMERIC_DIFFERENT"
        if a.operation != b.operation:
            return "NUMERIC_MATCH_SOURCE_DISTINCT"
        if a.orientation != b.orientation or a.ordering != b.ordering:
            return "SAME_COUNT_DIFFERENT_CONFIGURATION"
        return "SAME_CONFIGURATION_CANDIDATE"

    def compare(self) -> Dict[str, Any]:
        paths = [
            self.rphach_by_four_ab(),
            self.rphach_by_words_letters(),
            self.rphach_by_four_yhvhs(),
            self.orientation_variant(),
        ]
        comparisons = []
        for i, a in enumerate(paths):
            for b in paths[i + 1:]:
                comparisons.append({
                    "a": a.config_id,
                    "b": b.config_id,
                    "classification": self.classify(a, b),
                })
        return {
            "paths": [asdict(p) for p in paths],
            "comparisons": comparisons,
            "pair_spaces": self.pair_spaces(),
            "cycle_360_profile": self.modular_profile([72, 126, 230, 231, 288], 360),
            "rule": "Do not infer historical identity from numerical equality alone.",
        }

if __name__ == "__main__":
    import json
    print(json.dumps(RphachEngine().compare(), ensure_ascii=False, indent=2))

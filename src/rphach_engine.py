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

class RphachEngine:
    """Compare numeric, combinatorial and structural candidate paths.

    Equal numbers are deliberately not treated as equal structures.
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
        }

    @staticmethod
    def rphach_by_four_ab() -> PathResult:
        return PathResult(
            "C1", "4*72", ("AB", "SAG", "MA", "BAN"), 288,
            ("numeric_match", "four_blocks"),
            "four-name/filling representation",
        )

    @staticmethod
    def rphach_by_words_letters() -> PathResult:
        return PathResult(
            "C2", "72+216", ("72_words", "216_letters"), 288,
            ("numeric_match", "word_letter_decomposition"),
            "72 words + 216 letters representation",
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

    def compare(self) -> Dict[str, Any]:
        c1 = self.rphach_by_four_ab()
        c2 = self.rphach_by_words_letters()
        return {
            "paths": [asdict(c1), asdict(c2)],
            "same_output": c1.output == c2.output,
            "same_operation": c1.operation == c2.operation,
            "interpretation": (
                "NUMERIC_MATCH_SOURCE_DISTINCT"
                if c1.output == c2.output and c1.operation != c2.operation
                else "UNRESOLVED"
            ),
            "pair_spaces": self.pair_spaces(),
            "cycle_360_profile": self.modular_profile([72, 231, 230, 288], 360),
        }

if __name__ == "__main__":
    import json
    print(json.dumps(RphachEngine().compare(), ensure_ascii=False, indent=2))

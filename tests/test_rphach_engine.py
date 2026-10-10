from src.rphach_engine import RphachEngine

def test_base_counts():
    c = RphachEngine.base_counts()
    assert c["letters"] == 22
    assert c["unordered_pairs"] == 231
    assert c["ordered_pairs_no_repetition"] == 462
    assert c["ab"] == 72
    assert c["rphach"] == 288
    assert c["crystal_space_groups"] == 230
    assert c["cycle"] == 360

def test_two_rphach_paths_agree_numerically():
    engine = RphachEngine()
    a = engine.rphach_by_four_ab()
    b = engine.rphach_by_words_letters()
    assert a.output == 288
    assert b.output == 288
    assert a.operation != b.operation

def test_pair_spaces():
    assert RphachEngine.pair_spaces() == {
        "unordered_231": 231,
        "ordered_462": 462,
    }

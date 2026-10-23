from events.normalizers import normalize_name


def test_normalize_name():
    assert normalize_name("   aa    b   c") == "aa b c"
    assert normalize_name(" Python     Workshop") == "Python Workshop"

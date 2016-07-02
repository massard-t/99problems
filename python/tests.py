import P01


def test_P01_with_list_returns_last_one():
    assert 10 == P01.p01([0, 1, 8, 9, 10])

def test_P01_with_list_returns_last_two():
    assert 1 == P01.p01([5, 8, 2, 1])
import P01
import P02


def test_P01_with_list_returns_last_one():
    assert 10 == P01.p01([0, 1, 8, 9, 10])

def test_P01_with_list_returns_last_two():
    assert 1 == P01.p01([5, 8, 2, 1])

def test_P02_with_list_returns_pre_last_one():
    assert 8 == P02.p02([3, 4, 5, 6, 8, 210])

def test_P02_with_list_returns_pre_last_two():
    assert -2 == P02.p02([8, 4, 1, 4, 3, 4, 5, -2, 2])
import P01
import P02
import P03


def test_p01_with_list_returns_last_one():
    assert 10 == P01.func([0, 1, 8, 9, 10])


def test_p01_with_list_returns_last_two():
    assert 1 == P01.func([5, 8, 2, 1])


def test_p02_with_list_returns_pre_last_one():
    assert 8 == P02.func([3, 4, 5, 6, 8, 210])


def test_p02_with_list_returns_pre_last_two():
    assert -2 == P02.func([8, 4, 1, 4, 3, 4, 5, -2, 2])


def test_p03_with_list_returns_kth_elem_one():
    assert 3 == P03.func([3, 4, 3, 2, -3], 3)


def test_p03_with_list_returns_kth_elem_two():
    assert 0 == P03.func([0, 3, -3, 1, 3], 1)
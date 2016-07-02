import P01
import P02
import P03
import P04
import P05
import P06
import P07
import P08
import P09
import P10
import P11
import P12


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


def test_p04_with_list_returns_length_one():
    assert 3 == P04.func([0, 9, 10])


def test_p04_with_list_returns_length_two():
    assert 5 == P04.func([5, 5, 5, 5, 4])


def test_p05_with_list_returns_rev_one():
    assert [0, 4, 5, 6] == P05.func([6, 5, 4, 0])


def test_p05_with_list_returns_rev_two():
    assert [4, 3, 19] == P05.func([19, 3, 4])


def test_p06_with_palindrome_returns_true():
    assert True == P06.func([2, 5, 2])


def test_p06_with_not_palindrome_returns_false():
    assert False == P06.func([2, 3, 1, 8])


def test_p07_with_list_returns_flat_one():
    assert [1, 3, 4, 9, 10] == P07.funcl([1, [3, 4, 9], 10])


def test_p07_with_list_returns_flat_two():
    assert [10, 9, 10, 34, 2, 3, 6] == P07.funcl([[[10], 9, 10], 34, 2, 3, 6])


def test_p08_with_list_removes_dupes_one():
    assert [0, 10, 8] == P08.func([0, 0, 0, 0, 10, 10, 10, 8, 8, 8, 8])


def test_p08_with_list_removes_dupes_two():
    assert [1, -2, 5] == P08.func([1, 1, 1, -2, 5, 5, 5, 5, 5])


def test_p09_with_list_lists_dupes_one():
    assert [[0, 0, 0, 0], [10, 10, 10], [8, 8, 8, 8]] == P09.func([0, 0, 0, 0, 10, 10, 10, 8, 8, 8, 8])


def test_p09_with_list_lists_dupes_two():
    assert [[1, 1, 1], [-2], [5, 5, 5, 5, 5]] == P09.func([1, 1, 1, -2, 5, 5, 5, 5, 5])


def test_p10_with_list_lists_dupes_one():
    assert [[4, 0], [3, 10], [4, 8]] == P10.func([0, 0, 0, 0, 10, 10, 10, 8, 8, 8, 8])


def test_p10_with_list_lists_dupes_two():
    assert [[3, 1], [1, -2], [5, 5]] == P10.func([1, 1, 1, -2, 5, 5, 5, 5, 5])


def test_p11_with_list_lists_dupes_one():
    assert [[4, 0], [3, 10], 8] == P11.func([0, 0, 0, 0, 10, 10, 10, 8])


def test_p11_with_list_lists_dupes_two():
    assert [[3, 1], -2, [5, 5]] == P11.func([1, 1, 1, -2, 5, 5, 5, 5, 5])


def test_p12_with_list_lists_dupes_one():
    assert [0, 0, 0, 0, 10, 10, 10, 8] == P12.func([[4, 0], [3, 10], 8])


def test_p12_with_list_lists_dupes_two():
    assert [1, 1, 1, -2, 5, 5, 5, 5, 5] == P12.func([[3, 1], -2, [5, 5]])

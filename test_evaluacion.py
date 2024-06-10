import evaluacion as evals
import numpy as np
import pytest


def test_get_square_area_1():
    expected_result = 9
    assert evals.get_area_square(3) == expected_result

def test_get_square_area_2():
    expected_result = 6.25
    assert evals.get_area_square(2.5) == expected_result


def test_get_hypotenuse_2():
    expected_result = 4.196196
    assert evals.get_hypotenuse(3.1416, 2.7818) == pytest.approx(expected_result)


def test_reverse_list_1():
    vector = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected_result = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert evals.reverse_list(vector) == expected_result


def test_reverse_list_2():
    vector = ["a", "b", "c", "d", "e"]
    expected_result = ["e", "d", "c", "b", "a"]
    assert evals.reverse_list(vector) == expected_result


def test_get_indexes_1():
    vector = [11, 22, 33, 44]
    assert evals.get_indexes(vector, threshold=25) == [2, 3]


def test_get_indexes_2():
    vector = [11, 22, -33, 22]
    assert evals.get_indexes(vector, threshold=0) == [0, 1, 3]


def test_get_max_value_1():
    matrix = np.matrix('1 2; 3 4')
    assert evals.get_max_value_from(matrix) == 4


def test_get_max_value_2():
    matrix = np.matrix(np.arange(12).reshape((3, 4)))
    assert evals.get_max_value_from(matrix) == 11


def test_get_diagonal_values_1():
    matrix = np.array([0, 3])
    expected_result = evals.get_diagonal_values_from(np.arange(4).reshape(2, 2))
    assert np.array_equal(matrix, expected_result)



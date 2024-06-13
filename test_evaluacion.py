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


# Se agregan para hacer las pruebas que no vienen estructuradas en evaluacion
def test_remove_adjacent_to_nan():
    input_list = [6, 10, 5, 8, 9, np.nan, 23, 9, 7, 3, 21, 43, np.nan, 4, 6, 7, 8]
    expected_output = [6, 10, 5, 8, 9, 7, 3, 21, 6, 7, 8]
    assert evals.remove_adjacent_to_nan(input_list) == expected_output


def test_replicate_elements():
    vector_1 = [1, 2, 3]
    n_1 = 2
    expected_output_1 = [1, 1, 2, 2, 3, 3]
    assert evals.replicate_elements(vector_1, n_1) == expected_output_1

    vector_2 = [2, 1]
    n_2 = 0
    expected_output_2 = []
    assert evals.replicate_elements(vector_2, n_2) == expected_output_2


def test_extract_first_nonzero_digit():
    x = [1, 0.3, -2, 0.001, -0.0006, 582398, 3020]
    y = [1, 3, 2, 1, 6, 5, 3]
    expected_output_x = [1, 3, 2, 1, 6, 5, 3]
    expected_output_y = [1, 3, 2, 1, 6, 5, 3]
    assert evals.extract_first_nonzero_digit(x) == expected_output_x
    assert evals.extract_first_nonzero_digit(y) == expected_output_y


def test_remove_redundant_elements():
    input_vector = [5, 3, 6, 4, 7, 7, 3, 5, 9]
    expected_output = [5, 3, 6, 4, 7, 9]
    assert evals.remove_redundant_elements(input_vector) == expected_output

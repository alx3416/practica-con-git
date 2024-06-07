import evaluacion as evals


def test_get_indexes_1():
    vector = [11, 22, 33, 44]
    assert evals.get_indexes(vector, threshold=25) == [2, 3]


def test_get_indexes_2():
    vector = [11, 22, -33, 22]
    assert evals.get_indexes(vector, threshold=0) == [0, 1, 3]

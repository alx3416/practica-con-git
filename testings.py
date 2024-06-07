import pytest
import areas as ars


def test_get_square_area_1():
    assert ars.get_square_area(4) == 16


def test_get_square_area_2():
    assert ars.get_square_area(-9.5) == 0

def test_get_square_area_3():
    assert ars.get_square_area(0) == 0
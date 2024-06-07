import pytest
import areas as ars
import C1_TrianguloAsteriscos as C1


def test_get_square_area_1():
    assert ars.get_square_area(4) == 16


def test_get_square_area_2():
    assert ars.get_square_area(-9.5) == 0

def test_get_square_area_3():
    assert ars.get_square_area(0) == 0

def test_get_TrianguloAsteriscos_1():
    assert C1.TrianguloAsterisco(5) == 5

def test_get_TrianguloAsteriscos_2():
    assert C1.TrianguloAsterisco(-3) == 0

def test_get_TrianguloAsteriscos_3():
    assert C1.TrianguloAsterisco(5.5) == 5
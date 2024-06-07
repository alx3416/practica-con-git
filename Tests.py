#Programa para hacer tests.

import pytest
import Cambio_de_Temperatura as cdt



def test_celsius_a_farenheit():
    assert cdt.celsius_a_farenheit(1)==33.8

def test_farenheit_a_celsius():
    assert cdt.farenheit_a_celsius(1)==-17.22

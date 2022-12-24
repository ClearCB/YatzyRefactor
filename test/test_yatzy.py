from src.yatzy import Yatzy
import pytest


# Chance
# The player scores the sum of all dice, no matter what they read.
@pytest.mark.test_chance
def test_chance():

    assert 1 == Yatzy.chance([1])
    assert 14 == Yatzy.chance([1, 1, 3, 3, 6])
    assert 14 == Yatzy.chance([4, 5, 5])
    assert 9 == Yatzy.chance([4, 5])


# @pytest.fixture
# def inyector():
#     # Es el setup de unittest o de JUnit
#     tirada = Yatzy(1, 2, 3, 4, 5)
#     return tirada


# def test_fours(inyector):
#     # Es necesario un objeto ya creado
#     valorEsperado = 4
#     # No puedo testear con fixtures = inyeccion de dependencias
#     # los metodos estaticos como chance()
#     assert valorEsperado == inyector.fours()
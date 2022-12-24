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

# Yatzy
# The player scores 50 points if all the dice has the same value
@pytest.mark.test_yatzy
def test_yazty():

    assert 0 == Yatzy.yatzy([1,2])
    assert 50 == Yatzy.yatzy([2,2,2,2,2,2])
    assert 0 == Yatzy.yatzy([1,2,2,2,2,2,22])
    assert 50 == Yatzy.yatzy([1,1,1,1,1,1,1,1,1,1,1,1,1,1,1])


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
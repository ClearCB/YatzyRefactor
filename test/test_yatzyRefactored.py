from src.yatzyRefactored import Yatzy
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
    assert 50 == Yatzy.yatzy([2,2,2,2,2])
    assert 0 == Yatzy.yatzy([1,2,2,2,2])
    assert 50 == Yatzy.yatzy([1,1,1,1,1])

# Counting Numbers
# The player scores the sum of the dice that has the same number which was selected
@pytest.mark.test_countingNumbers
def test_countingNumbers():

    assert 1 == Yatzy.countingNumbers(1,[1,2,3,5,6])
    assert 4 == Yatzy.countingNumbers(2,[2,2,1,1,5])
    assert 9 == Yatzy.countingNumbers(3,[3,3,3,1,1])
    assert 16 == Yatzy.countingNumbers(4,[4,4,4,4,6])
    assert 25 == Yatzy.countingNumbers(5,[5,5,5,5,5])
    assert 30 == Yatzy.countingNumbers(6,[6,6,6,6,6])

# Pair
# The player score the sum of the highest paired number
@pytest.mark.test_scorePair
def test_scorePair():

    assert 0 == Yatzy.highestPair([1,2,3,4,5])
    assert 2 == Yatzy.highestPair([1,1,1,3,2])
    assert 4 == Yatzy.highestPair([1,1,2,2,2])
    assert 6 == Yatzy.highestPair([3,3,5,6,4])
    assert 8 == Yatzy.highestPair([4,4,4,4,4])
    assert 10 == Yatzy.highestPair([5,5,2,3,3])
    assert 12 == Yatzy.highestPair([6,6,5,6,5])

# Two pairs
# The player score the sum of the two paired numbers
@pytest.mark.test_scoreDoublePair
def test_scoreDoublePair():

    assert 0 == Yatzy.twoPair([1,1,1,2,3])
    assert 6 == Yatzy.twoPair([1,1,4,2,2])
    assert 10 == Yatzy.twoPair([2,2,3,3,5])
    assert 8 == Yatzy.twoPair([3,3,1,1,4])
    assert 14 == Yatzy.twoPair([3,3,4,4,5])
    assert 18 == Yatzy.twoPair([4,4,5,5,6])
    assert 16 == Yatzy.twoPair([6,6,2,2,6])
    assert 24 == Yatzy.twoPair([6,6,6,6,1])


# Three of a kind
# The player score the sum of the third dice that has the same value
@pytest.mark.test_threeOfAKind
def test_threeOfAKind():

    assert 0 == Yatzy.threeOfAKind([1,1,2,2,3])
    assert 3 == Yatzy.threeOfAKind([1,1,1,1,2])
    assert 6 == Yatzy.threeOfAKind([2,2,2,2,2])
    assert 9 == Yatzy.threeOfAKind([3,3,3,6,3])
    assert 12 == Yatzy.threeOfAKind([4,4,4,4,2])
    assert 15 == Yatzy.threeOfAKind([5,5,5,5,3])
    assert 18 == Yatzy.threeOfAKind([6,6,6,6,6])

# Four of a kind
# The player score the sum of the four dice that has the same values
@pytest.mark.test_fourOfAKind
def test_fourOfAKind():

    assert 0 == Yatzy.fourOfAKind([1,1,1,2,2])
    assert 4 == Yatzy.fourOfAKind([1,1,1,1,2])
    assert 8 == Yatzy.fourOfAKind([2,2,2,2,2])
    assert 12 == Yatzy.fourOfAKind([3,3,3,3,6])
    assert 16 == Yatzy.fourOfAKind([4,4,4,4,2])
    assert 20 == Yatzy.fourOfAKind([5,5,5,5,3])
    assert 24 == Yatzy.fourOfAKind([6,6,6,6,6])

# SmallStraight
# The player scores 15 if there is a straight at the dice (4 numbers in ascendent order)
@pytest.mark.test_smallStraight
def test_smallStraight():

    assert 15 == Yatzy.smallStraight([1,2,3,4,5])
    assert 17 == Yatzy.smallStraight([2,3,4,5,3])
    assert 17 == Yatzy.smallStraight([5,3,2,4,3])
    assert 20 == Yatzy.smallStraight([6,3,4,2,5])
    assert 0 == Yatzy.smallStraight([1,1,2,3,5])
    assert 0 == Yatzy.smallStraight([1,1,2,3,6])
    assert 0 == Yatzy.smallStraight([6,5,4,2,1])

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
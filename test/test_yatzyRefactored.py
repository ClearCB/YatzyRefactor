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



# # Counting Numbers
# # The player scores the sum of the dice that has the same number which was selected
# @pytest.mark.test_countingNumbers
# def test_countingNumbers():

#     assert 1 == Yatzy.countingNumbers(1,[1,2,3,5,6])
#     assert 4 == Yatzy.countingNumbers(2,[2,2,1,1,5])
#     assert 9 == Yatzy.countingNumbers(3,[3,3,3,1,1])
#     assert 16 == Yatzy.countingNumbers(4,[4,4,4,4,6])
#     assert 25 == Yatzy.countingNumbers(5,[5,5,5,5,5])
#     assert 30 == Yatzy.countingNumbers(6,[6,6,6,6,6])



# ones
# The player scores the sum of total ones dice at the dice values
@pytest.mark.test_ones
def test_ones():

    assert 1 == Yatzy.ones([1,2,3,4,5])
    assert 0 == Yatzy.ones([6,2,3,4,5])
    assert 5 == Yatzy.ones([1,1,1,1,1])

# twos
# The player scores the sum of total twos dice at the dice values
@pytest.mark.test_twos
def test_twos():

    assert 2 == Yatzy.twos([1,2,3,4,5])
    assert 0 == Yatzy.twos([1,6,3,4,5])
    assert 10 == Yatzy.twos([2,2,2,2,2])

# threes
# The player scores the sum of total threes dice at the dice values
@pytest.mark.test_threes
def test_threes():

    assert 3 == Yatzy.threes([1,2,3,4,5])
    assert 0 == Yatzy.threes([1,2,6,4,5])
    assert 15 == Yatzy.threes([3,3,3,3,3])

# fours
# The player scores the sum of total fours dice at the dice values
@pytest.mark.test_fours
def test_fours():

    assert 4 == Yatzy.fours([1,2,3,4,5])
    assert 0 == Yatzy.fours([1,2,3,6,5])
    assert 20 == Yatzy.fours([4,4,4,4,4])

# fives
# The player scores the sum of total fives dice at the dice values
@pytest.mark.test_fives
def test_fives():

    assert 5 == Yatzy.fives([1,2,3,4,5])
    assert 0 == Yatzy.fives([1,2,3,4,6])
    assert 25 == Yatzy.fives([5,5,5,5,5])

# sixs
# The player scores the sum of total sixs dice at the dice values
@pytest.mark.test_sixs
def test_sixs():

    assert 6 == Yatzy.sixs([1,2,3,4,6])
    assert 0 == Yatzy.sixs([1,2,3,4,1])
    assert 30 == Yatzy.sixs([6,6,6,6,6])

# Highest Pair
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

# Paired number
# The player scores the sum of the value repeated exactly 2 times
@pytest.mark.test_pair
def test_pair():

    assert 0 == Yatzy.pair([1,1,1,2,3])
    assert 2 == Yatzy.pair([1,1,5,2,3])

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
# The player scores 15 points if there is a straight at the dice (4 numbers in ascendent order)
@pytest.mark.test_smallStraight
def test_smallStraight():

    assert 15 == Yatzy.smallStraight([1,2,3,4,5])
    assert 0 == Yatzy.smallStraight([6,5,4,2,1])

# LargeStraight
# The player scores 20 points if there is a straight at the dice (5 numbers in ascendent order)
@pytest.mark.test_largeStraight
def test_largeStraight():

    assert 20 == Yatzy.largeStraight([6,3,4,2,5])
    assert 0 == Yatzy.largeStraight([5,3,2,4,3])

# Full-House
# The player scores 25 points if there are 2 values of the same kind and the other 3 has teh same value but different the first
@pytest.mark.test_fullHouse
def test_fullHouse():

    assert 8 == Yatzy.fullHouse([1,1,2,2,2])
    assert 28 == Yatzy.fullHouse([5,5,6,6,6])
    assert 0 == Yatzy.fullHouse([1,1,2,2,3])
    assert 0 == Yatzy.fullHouse([1,2,2,2,3])
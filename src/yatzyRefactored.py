class Yatzy:

    def __init__(self, d1, d2, d3, d4, _5):
        self.dice = [0]*5
        self.dice[0] = d1
        self.dice[1] = d2
        self.dice[2] = d3
        self.dice[3] = d4
        self.dice[4] = _5

    @staticmethod
    def chance(diceList):
        total = sum(diceList)
        return total

    @staticmethod
    def yatzy(diceList):

        valueRepeated = diceList.count(diceList[0])
        numberOfDice = len(diceList)

        if valueRepeated == numberOfDice:
            return 50
        else:
            return 0

    @staticmethod
    def countingNumbers(numberChosen, diceList):

        numberCount = diceList.count(numberChosen)
        total = numberChosen * numberCount
        return total

    @staticmethod
    def highestPair(diceList):

        for num in range(6,0,-1):

            numCount = diceList.count(num)
            if numCount >= 2:

                return num*2

        return 0

    @staticmethod
    def twoPair(diceList):

        numPaired = 0
        total = 0
        num = 6

        while numPaired <= 2 and num >=1 :

            numCount = diceList.count(num)

            if numCount >= 4:

                total = num * 4
                return total

            if numCount >=2:

                numPaired += 1
                total += num*2

            num -= 1

        if numPaired == 2:

            return total
        
        else:
            return 0
    
    @staticmethod
    def threeOfAKind(diceList):

        for num in range(6,0,-1):

            numCount = diceList.count(num)

            if numCount >= 3:

                return num * 3

        return 0

    @staticmethod
    def fourOfAKind(diceList):

        for num in range(6,0,-1):

            numCount = diceList.count(num)

            if numCount >= 4:

                return num * 4

        return 0

    @staticmethod
    def smallStraight(diceList):

        diceListSorted = sorted(diceList)
        straightNumbers = list(range(min(diceList),max(diceList)+1))

        for num in range(1,7):

            numCount = diceList.count(num)

            if numCount != 1 and num in diceList:

                diceListSorted.remove(num)
    
        if diceListSorted == straightNumbers:

            return Yatzy.chance(diceList)

        return 0


    # @staticmethod
    # def largeStraight(diceList):

    #     for num in diceList:

    #         numCount = diceList.count(num)

    #         if numCount != 1:
    #             return 0

    #     return Yatzy.chance(diceList)

    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0

if __name__ == '__main__':

    assert 15 == Yatzy.smallStraight([1,2,3,4,5])
    assert 17 == Yatzy.smallStraight([2,3,4,5,3])
    assert 17 == Yatzy.smallStraight([5,3,2,4,3])
    assert 20 == Yatzy.smallStraight([6,3,4,2,5])
    assert 0 == Yatzy.smallStraight([1,1,2,3,5])
    assert 0 == Yatzy.smallStraight([1,1,2,3,6])
    assert 0 == Yatzy.smallStraight([6,5,4,2,1])
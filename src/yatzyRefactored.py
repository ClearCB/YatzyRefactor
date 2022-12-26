class Yatzy:

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

    # @staticmethod
    # def countingNumbers(numberChosen, diceList):

    #     numberCount = diceList.count(numberChosen)
    #     total = numberChosen * numberCount
    #     return total

    @staticmethod
    def ones(diceList):
        return diceList.count(1) * 1

    @staticmethod
    def twos(diceList):
        return diceList.count(2) * 2

    @staticmethod
    def threes(diceList):
        return diceList.count(3) * 3

    @staticmethod
    def fours(diceList):
        return diceList.count(4) * 4

    @staticmethod
    def fives(diceList):
        return diceList.count(5) * 5

    @staticmethod
    def sixs(diceList):
        return diceList.count(6) * 6

    @staticmethod
    def highestPair(diceList):

        for num in range(6,0,-1):

            numCount = diceList.count(num)
            if numCount >= 2:

                return num*2

        return 0

    @staticmethod
    def pair(diceList):

        for num in range(6,0,-1):

            numCount = diceList.count(num)
            if numCount == 2:

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

        for num in range(1,6):

            numCount = diceList.count(num)

            if numCount != 1:
                return 0

        return 15

    @staticmethod
    def largeStraight(diceList):

        for num in range(2,7):

            numCount = diceList.count(num)

            if numCount != 1:
                return 0

        return 20

    @staticmethod
    def fullHouse(diceList):

        if Yatzy.threeOfAKind(diceList) and Yatzy.pair(diceList): 
            return Yatzy.threeOfAKind(diceList) + Yatzy.pair(diceList)
        
        else:
            return 0
'''
This class allows a player to select the points that would get positioning the dice into the category they choose

Each method is a category, so when selected, return the points that the player gets
'''
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
        ONE = 1
        return diceList.count(1) * ONE

    @staticmethod
    def twos(diceList):
        TWO = 2
        return diceList.count(2) * TWO

    @staticmethod
    def threes(diceList):
        THREE = 3
        return diceList.count(3) * THREE

    @staticmethod
    def fours(diceList):
        FOUR = 4
        return diceList.count(4) * FOUR

    @staticmethod
    def fives(diceList):
        FIVE = 5
        return diceList.count(5) * FIVE

    @staticmethod
    def sixs(diceList):
        SIX = 6
        return diceList.count(6) * SIX

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
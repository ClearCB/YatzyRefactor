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
        total = numberCount * numberCount
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
    def four_of_a_kind(diceList):

        for num in range(6,0,-1):

            numCount = diceList.count(num)

            if num >= 4:

                return num * 4
                
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

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

# if __name__ == '__main__':


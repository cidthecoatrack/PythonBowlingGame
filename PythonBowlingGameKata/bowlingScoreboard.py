class bowlingScoreboard():
    def __init__(self):
        self.rolls = []

    def addRoll(self, roll):
        self.rolls.append(roll)

    def getScore(self):
        score = 0

        for index, roll in enumerate(self.rolls):
            score += roll

            strikeMultiplier = self.getStrikeMultiplier(index)
            score += roll * strikeMultiplier

            if strikeMultiplier == 0 and self.addToSpare(index):
                score += roll

        return score

    def getStrikeMultiplier(self, index):
        multiplier = 0

        if index > 0 and index < 10 and self.rolls[index - 1] == 10:
            multiplier += 1

        if index > 1 and index < 11 and self.rolls[index - 2] == 10:
            multiplier += 1

        return multiplier

    def addToSpare(self, index):
        return index > 1 and self.rolls[index - 1] + self.rolls[index - 2] == 10
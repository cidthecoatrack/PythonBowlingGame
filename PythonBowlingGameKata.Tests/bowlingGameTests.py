import unittest
import sys
sys.path.append('../PythonBowlingGameKata')

import bowlingScoreboard

class Test_bowlingTests(unittest.TestCase):

    def setUp(self):
        self.scoreboard = bowlingScoreboard.bowlingScoreboard()

    def test_gutterBallGame(self):
        for x in range(0, 20):
            self.scoreboard.addRoll(0)

        score = self.scoreboard.getScore()
        self.assertEqual(score, 0)

    def test_onePinEachThrow(self):
        for x in range(0, 20):
            self.scoreboard.addRoll(1)

        score = self.scoreboard.getScore()
        self.assertEqual(score, 20)

    def test_throwASpare(self):
        self.scoreboard.addRoll(8)
        self.scoreboard.addRoll(2)
        self.scoreboard.addRoll(3)

        for x in range(0, 17):
            self.scoreboard.addRoll(0)

        score = self.scoreboard.getScore()
        self.assertEqual(score, 16)

    def test_throwAStrike(self):
        self.scoreboard.addRoll(10)
        self.scoreboard.addRoll(3)
        self.scoreboard.addRoll(4)

        for x in range(0, 17):
            self.scoreboard.addRoll(0)

        score = self.scoreboard.getScore()
        self.assertEqual(score, 24)

    def test_perfectGame(self):
        for x in range(0, 12):
            self.scoreboard.addRoll(10)

        score = self.scoreboard.getScore()
        self.assertEqual(score, 300)

if __name__ == '__main__':
    unittest.main()
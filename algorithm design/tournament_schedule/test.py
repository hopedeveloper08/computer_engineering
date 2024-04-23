import unittest
from model import tournaments_schedule


class TestTournamentSchedule(unittest.TestCase):

    def test_tournament_schedule_2_team(self):
        teams = tournaments_schedule(2)
        self.assertEqual(teams[1], [2])
        self.assertEqual(teams[2], [1])

    def test_tournament_schedule_3_team(self):
        teams = tournaments_schedule(3)
        self.assertEqual(teams[1], [2, 3, '-'])
        self.assertEqual(teams[2], [1, '-', 3])
        self.assertEqual(teams[3], ['-', 1, 2])

    def test_tournament_schedule_7_team(self):
        teams = tournaments_schedule(7)
        self.assertEqual(teams[1], [2, 3, 4, 5, 6, 7, '-'])
        self.assertEqual(teams[2], [1, 4, 3, '-', 5, 6, 7])
        self.assertEqual(teams[3], [4, 1, 2, 7, '-', 5, 6])
        self.assertEqual(teams[4], [3, 2, 1, 6, 7, '-', 5])
        self.assertEqual(teams[5], [6, 7, '-', 1, 2, 3, 4])
        self.assertEqual(teams[6], [5, '-', 7, 4, 1, 2, 3])
        self.assertEqual(teams[7], ['-', 5, 6, 3, 4, 1, 2])

    def test_tournament_schedule_12_team(self):
        teams = tournaments_schedule(12)
        self.assertEqual(teams[1], [2, 3, 4, 6, 5, 7, 8, 9, 10, 11, 12])
        self.assertEqual(teams[2], [1, 5, 3, 4, 6, 12, 7, 8, 9, 10, 11])
        self.assertEqual(teams[3], [6, 1, 2, 5, 4, 11, 12, 7, 8, 9, 10])
        self.assertEqual(teams[4], [5, 6, 1, 2, 3, 10, 11, 12, 7, 8, 9])
        self.assertEqual(teams[5], [4, 2, 6, 3, 1, 9, 10, 11, 12, 7, 8])
        self.assertEqual(teams[6], [3, 4, 5, 1, 2, 8, 9, 10, 11, 12, 7])
        self.assertEqual(teams[7], [8, 9, 10, 12, 11, 1, 2, 3, 4, 5, 6])
        self.assertEqual(teams[8], [7, 11, 9, 10, 12, 6, 1, 2, 3, 4, 5])
        self.assertEqual(teams[9], [12, 7, 8, 11, 10, 5, 6, 1, 2, 3, 4, ])
        self.assertEqual(teams[10], [11, 12, 7, 8, 9, 4, 5, 6, 1, 2, 3])
        self.assertEqual(teams[11], [10, 8, 12, 9, 7, 3, 4, 5, 6, 1, 2])
        self.assertEqual(teams[12], [9, 10, 11, 7, 8, 2, 3, 4, 5, 6, 1])

    def test_tournament_schedule_10_team(self):
        teams = tournaments_schedule(10)
        self.assertEqual(teams[1], [2, 3, 4, 6, 5, 10, 9, 8, 7])
        self.assertEqual(teams[2], [1, 5, 3, 4, 7, 6, 10, 9, 8])
        self.assertEqual(teams[3], [8, 1, 2, 5, 4, 7, 6, 10, 9])
        self.assertEqual(teams[4], [5, 9, 1, 2, 3, 8, 7, 6, 10])
        self.assertEqual(teams[5], [4, 2, 10, 3, 1, 9, 8, 7, 6])
        self.assertEqual(teams[6], [7, 8, 9, 1, 10, 2, 3, 4, 5])
        self.assertEqual(teams[7], [6, 10, 8, 9, 2, 3, 4, 5, 1])
        self.assertEqual(teams[8], [3, 6, 7, 10, 9, 4, 5, 1, 2])
        self.assertEqual(teams[9], [10, 4, 6, 7, 8, 5, 1, 2, 3])
        self.assertEqual(teams[10], [9, 7, 5, 8, 6, 1, 2, 3, 4])

    def test_tournament_schedule_9_team(self):
        teams = tournaments_schedule(9)
        self.assertEqual(teams[1], [2, 3, 4, 6, 5, '-', 9, 8, 7])
        self.assertEqual(teams[2], [1, 5, 3, 4, 7, 6, '-', 9, 8])
        self.assertEqual(teams[3], [8, 1, 2, 5, 4, 7, 6, '-', 9])
        self.assertEqual(teams[4], [5, 9, 1, 2, 3, 8, 7, 6, '-'])
        self.assertEqual(teams[5], [4, 2, '-', 3, 1, 9, 8, 7, 6])
        self.assertEqual(teams[6], [7, 8, 9, 1, '-', 2, 3, 4, 5])
        self.assertEqual(teams[7], [6, '-', 8, 9, 2, 3, 4, 5, 1])
        self.assertEqual(teams[8], [3, 6, 7, '-', 9, 4, 5, 1, 2])
        self.assertEqual(teams[9], ['-', 4, 6, 7, 8, 5, 1, 2, 3])


if __name__ == '__main__':
    unittest.main()

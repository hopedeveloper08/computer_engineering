import unittest
from greedy_knapsack import knapsack


class TestKnapsack(unittest.TestCase):
    def test_knapsack(self):
        capacity = 4
        objects = [
            {'weight': 2, 'value': 10},
            {'weight': 3, 'value': 7},
            {'weight': 1, 'value': 2},
            {'weight': 4, 'value': 6},
            {'weight': 3, 'value': 3}
        ]

        choices, values = knapsack(capacity, objects)

        self.assertEqual([1, 3], choices)
        self.assertEqual(12, values)

        self.assertNotEqual(17, values)
        self.assertNotEqual([1, 2], choices)


if __name__ == '__main__':
    unittest.main()

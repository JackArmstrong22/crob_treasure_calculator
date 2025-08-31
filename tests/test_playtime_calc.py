import unittest
from playtime_calc import playtime_calc

LEVEL_ONE = 1


class TestPlaytime(unittest.TestCase):
    def test1(self):
        self.assertEqual(playtime_calc(LEVEL_ONE, 0), "Invalid time!")

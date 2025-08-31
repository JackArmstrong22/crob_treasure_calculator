import unittest
from playtime_calc import playtime_calc

LEVEL_ONE = 1


class TestPlaytime(unittest.TestCase):
    def test1(self):
        self.assertEqual(playtime_calc(LEVEL_ONE, 0), "Invalid time!")

    def test2(self):
        typewriter = 2026080
        self.assertEqual(playtime_calc(LEVEL_ONE, 24), typewriter)

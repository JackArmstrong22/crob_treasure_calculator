import unittest
from playtime_calc import playtime_calc


class TestPlaytime(unittest.TestCase):
    def test1(self):
        self.assertEqual(playtime_calc(0), "Invalid time!")

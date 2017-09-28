import unittest
from main import sum

class TestMain(unittest.TestCase):
    def test__sum(self):
        test_set = [(1, 2), (2, 3), (2, 0)]
        ans = [3, 5, 2]
        actual = []

        for test in test_set:
            actual.append(sum(test[0], test[1]))


        self.assertEqual(actual, ans)

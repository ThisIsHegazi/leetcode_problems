import unittest
from main import Solution


class TestRoman(unittest.TestCase):
    def test_convert_static(self):
        test1 = "III"
        test2 = "LVIII"
        test3 = "MCMXCIV"
        try:
            self.assertEqual(Solution.romanToInt(test1), 3)
            print(f"test {test1} PASS")
            self.assertEqual(Solution.romanToInt(test2), 55)
            print(f"test {test2} PASS")
            self.assertEqual(Solution.romanToInt(test3), 1994)
            print(f"test {test3} PASS")
        except AssertionError as err:
            print(f"FAIL")
            print(err)


if __name__ == "__main__":
    unittest.main()

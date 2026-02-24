import unittest
from main import Solution


class TestRoman(unittest.TestCase):
    def test_convert_static(self):
        test1 = Solution()
        test2 = Solution()
        test3 = Solution()
        try:
            self.assertEqual(
                test1.longestCommonPrefix(["flower", "flow", "flight"]), "fl"
            )
            print(f"test1 PASS")
            self.assertEqual(test2.longestCommonPrefix(["dog", "racecar", "car"]), "")
            print(f"test2 PASS")
        except AssertionError as err:
            print(f"FAIL")
            print(err)


if __name__ == "__main__":
    unittest.main()

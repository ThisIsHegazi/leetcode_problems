import unittest
from main import Solution


class TestRoman(unittest.TestCase):
    def test_convert_static(self):
        test1 = Solution()
        test2 = Solution()
        test3 = Solution()
        try:
            self.assertEqual(test1.isValid("()"), True)
            print(f"test1 PASS")
            self.assertEqual(test2.isValid("()[]{}"), True)
            print(f"test2 PASS")
            self.assertEqual(test3.isValid("(]"), False)
            print(f"test3 PASS")
        except AssertionError as err:
            print(f"FAIL")
            print(err)


if __name__ == "__main__":
    unittest.main()

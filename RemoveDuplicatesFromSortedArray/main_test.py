import unittest
from main import Solution


class TestRoman(unittest.TestCase):
    def test_convert_static(self):
        test1 = Solution()
        test2 = Solution()
        test3 = Solution()
        try:
            self.assertEqual(test1.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]), 5)
            print(f"test1 PASS")
            self.assertEqual(test2.removeDuplicates([1, 1, 2]), 2)
            print(f"test2 PASS")
        except AssertionError as err:
            print(f"FAIL")
            print(err)


if __name__ == "__main__":
    unittest.main()

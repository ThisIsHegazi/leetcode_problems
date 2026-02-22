class Solution:
    @staticmethod
    def romanToInt(s: str) -> int:
        char_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        subtract_dict = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
        result = 0
        for i in range(len(s)):
            if (
                i < len(s) - 1
                and s[i] in subtract_dict.keys()
                and s[i + 1] in subtract_dict[s[i]]
            ):
                result -= char_dict[s[i]]
            else:
                result += char_dict[s[i]]
        return result

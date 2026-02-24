class Solution:

    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort()
        loop_count = len(strs[0])
        counter = 0
        for i in range(loop_count):
            if strs[0][i] == strs[-1][i]:
                counter += 1
            else:
                return strs[0][:counter]
        return strs[0][:counter]

class Solution:
    def searchInsert(self, nums: list[int], target: int):
        low = 0
        high = len(nums) - 1
        while low <= high:
            if target < nums[low]:
                return low
            if target > high:
                return high + 1
            midpoint = (low + high) // 2
            if target == nums[midpoint]:
                return midpoint
            if target > nums[midpoint]:
                low = midpoint + 1
            else:
                high = midpoint - 1

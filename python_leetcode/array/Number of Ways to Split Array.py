"""
You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

"""

from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        s = sum(nums)
        ans = t = 0
        for x in nums[:-1]:
            t += x
            ans += t >= s - t
        return ans
        

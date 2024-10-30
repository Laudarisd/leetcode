"""
Problem: https://leetcode.com/problems/intersection-of-two-arrays-ii/
"""


import numpy as np

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        inter_sec = []
        for i in nums1:
            if i in nums2:
                inter_sec.append(i)
                nums2.remove(i)
        return inter_sec
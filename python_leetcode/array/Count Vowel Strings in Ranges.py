"""
You are given a 0-indexed array of strings words and a 2D array of integers queries.

Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.

Return an array ans of size queries.length, where ans[i] is the answer to the ith query.

Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

"""


from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = set('aeiou')
        nums = [i for i, w in enumerate(words) if w[0] in vowels and w[-1] in vowels]
        return[bisect_left(nums, l) - bisect_left(nums, r) + int(words[r][0] in vowels and words[r][-1] in vowels) for l, r in queries]
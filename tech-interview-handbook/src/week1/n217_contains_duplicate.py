from typing import List


class Solution:
    """
    Given an integer array nums, return true if any value appears at least twice in the array,
    and return false if every element is distinct.
    """

    def contains_duplicate(self, nums: List[int]) -> bool:
        """time complexity: O(1) space complexity: O(n)"""
        nums_set = set(nums)
        return len(nums_set) != len(nums)

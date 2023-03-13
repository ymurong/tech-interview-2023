from typing import List


class Solution:
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.

    You can return the answer in any order.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

    Input: nums = [3,2,4], target = 6
    Output: [1,2]
    """

    def two_sum_1(self, nums: List[int], target: int) -> List[int]:
        """O(n) time, O(n) space"""
        inverse_idx = {}
        for idx, num in enumerate(nums):
            match = target - num
            if match in inverse_idx:
                return [inverse_idx[match], idx]
            inverse_idx[num] = idx

    def two_sum_2(self, nums: List[int], target: int) -> List[int]:
        """O(nlog(n)) time, O(1) space"""
        nums = sorted(enumerate(nums), key=lambda i: i[1])
        left = 0
        right = len(nums) - 1
        while left <= right:
            sum = nums[left][1] + nums[right][1]
            if sum == target:
                # original index
                return [nums[left][0], nums[right][0]]
            if sum > target:
                right -= 1
            if sum < target:
                left += 1
        return []

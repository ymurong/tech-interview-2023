from typing import List


class Solution:
    """
    Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.

    Input: nums = [-1,0,1,2,-1,-4]
    Output: [[-1,-1,2],[-1,0,1]]
    Explanation:
    nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
    nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
    nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
    The distinct triplets are [-1,0,1] and [-1,-1,2].
    Notice that the order of the output and the order of the triplets does not matter.

    Input: nums = [0,1,1]
    Output: []
    Explanation: The only possible triplet does not sum up to 0.

    Input: nums = [0,0,0]
    Output: [[0,0,0]]
    Explanation: The only possible triplet sums up to 0.
    """

    def three_sum(self, nums: List[int]) -> List[List[int]]:
        """time complexity: O(n^2) space complexity: O(n)"""
        nums = sorted(enumerate(nums), key=lambda x: x[1])
        results = set()
        for i in range(len(nums)):
            cn = nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left][1] + nums[right][1] + cn[1]
                if sum == 0:
                    results.add((cn[1], nums[left][1], nums[right][1]))
                    left += 1
                    right -= 1
                elif sum > 0:
                    right -= 1
                else:
                    # sum < 0
                    left += 1
        # transform set of set to list of list
        return [list(r) for r in results]

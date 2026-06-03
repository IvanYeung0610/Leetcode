"""
Ivan Yeung

1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_index: dict[int, int] = {}
        # Create a map of nums to their relative index
        for i in range(len(nums)):
            nums_index[nums[i]] = i

        # Iterate through the list again and find the matching pair
        for i in range(len(nums)):
            target_pair = target - nums[i]
            if (target_pair in nums_index) and (nums_index[target_pair] != i):
                return [i, nums_index[target_pair]]
        return []

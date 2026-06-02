"""
Ivan Yeung

217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        num_set: set[int] = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)
        return False

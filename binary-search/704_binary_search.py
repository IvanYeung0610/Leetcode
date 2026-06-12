"""
Ivan Yeung

704. Binary Search
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        start: int = 0
        end: int = len(nums) - 1
        while (start <= end):
            pivot: int = start + ((end - start) // 2)
            if (nums[pivot] > target):
                end = pivot - 1
            elif (nums[pivot] < target):
                start = pivot + 1
            else:
                return pivot

        return -1

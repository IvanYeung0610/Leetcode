"""
Ivan Yeung

4. Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).
"""
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # make sure that nums1 is always the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        total = len(nums1) + len(nums2)
        half = total // 2

        # binary search on the smaller array to find left partition
        left = 0
        right = len(nums1) - 1

        while left <= right:
            # the index we are taking up to from the smaller array
            mid = left + ((right - left) // 2)
            # the index we are taking up to from the larger array
            larger_index = half - (mid + 2)

            if ()

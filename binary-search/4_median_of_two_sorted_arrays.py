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

        while True:
            # the index we are taking up to from the smaller array
            mid = left + ((right - left) // 2)
            # the index we are taking up to from the larger array
            remaining = half - (mid + 2)

            # Set up variables for partition boundary of smaller array
            if mid >= 0:
                nums1Left = nums1[mid]
            else:
                nums1Left = float("-infinity")

            if (mid + 1) < len(nums1):
                nums1Right = nums1[mid + 1]
            else:
                nums1Right = float("infinity")

            # Set up variables for partition boundary of larger array
            if remaining >= 0:
                nums2Left = nums2[remaining]
            else:
                nums2Left = float("-infinity")

            if (remaining + 1) < len(nums2):
                nums2Right = nums2[remaining + 1]
            else:
                nums2Right = float("infinity")

            # caculate median once valid partitions have been found
            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                # case where the median is just middle number since total is odd
                if total % 2 != 0:
                    return min(nums1Right, nums2Right)
                # case where average needs to be taken since total is even
                return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2

            # Binary Search Adjustments
            elif nums1Left > nums2Right:
                right = mid - 1
            else:
                left = mid + 1

        return 0


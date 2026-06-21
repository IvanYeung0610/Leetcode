"""
Ivan Yeung

33. Search in Rotated Sorted Array
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""
class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            # check if mid is the the target
            if nums[mid] == target:
                return mid

            # mid and right are in the same segment
            if nums[mid] < nums[right]:
                if target > nums[mid] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # mid and left are in the same segment
            else: 
                if target < nums[mid] and target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

"""
NOTE: This is just binary search that just deals with the extra cases that comes with
the rotation of the array. This is resolved by basing the choice of moving the left or
right pointer on the segment that is sorted. Aka the bounds of the two points that are
together. Since we know at least one of the following has to be true:
    - left and mid are sorted together in the same segment
    = right and mid are sorted together in the same segment
"""

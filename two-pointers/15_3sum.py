"""
Ivan Yeung

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets: list[list[int]] = []

        nums.sort() # sort the list

        for i in range(len(nums)):
            # only find triplets on unique first numbers
            if (i == 0) or (nums[i] != nums[i-1]):
                target_pair_sum = -(nums[i])

                left = i + 1
                right = len(nums) - 1

                while left < right:
                    if nums[left] + nums[right] == target_pair_sum:
                        # add triplet to return list
                        triplets.append([nums[i], nums[left], nums[right]])
                        # move left and right pointer to unique numbers
                        left += 1
                        right -= 1
                        while (left < right) and (nums[left] == nums[left-1]):
                            left += 1
                        while (left < right) and (nums[right] == nums[right+1]):
                            right -= 1
                    elif nums[left] + nums[right] > target_pair_sum:
                        # decrement right pointer since sum is too big
                        right -= 1
                    else: # nums[left] + nums[right] < target_pair_sum: 
                        # increment left pointer since sum is too small
                        left += 1

        return triplets

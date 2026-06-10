"""
Ivan Yeung

42. Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""
class Solution:
    def trap(self, height: list[int]) -> int:
        # formula for finding water stored at current index:
        # min(maxLeft, maxRight) - height[i]
        water_trapped = 0
        # two pointers
        left = 0
        right = len(height) - 1
        # max values found as pointers move inwards
        maxLeft = height[left]
        maxRight = height[right]

        while left < right:
            if height[left] < height[right]:
                # move left pointer and calculate water
                left += 1
                # NOTE: we don't have to check if left == right since the
                # result of the curr_water will always be <=0
                curr_water = min(maxLeft, maxRight) - height[left]
                if curr_water > 0:
                    water_trapped += curr_water
                maxLeft = max(maxLeft, height[left])
            else:
                # move right pointer and calculate water
                right -= 1
                curr_water = min(maxLeft, maxRight) - height[right]
                if curr_water > 0:
                    water_trapped += curr_water
                maxRight = max(maxRight, height[right])

        return water_trapped

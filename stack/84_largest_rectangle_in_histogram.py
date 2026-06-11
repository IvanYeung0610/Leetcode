"""
Ivan Yeung

84. Largest Rectangle in Histogram
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.
"""
class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        max_area: int = 0
        # store a monotonically increasing stack of the heights (store the index and height)
        stack: list[tuple[int, int]] = []
        for i in range(len(heights)):
            left_bound: int = i
            while len(stack) != 0 and stack[-1][1] > heights[i]:
                # when we pop a height index, we compute the total area of that rectangle
                # at that height for as far as it goes (which is up the the current index)
                bar = stack.pop()
                # we also store the index since this bar is taller than the current bar so the left
                # boundary that it can be expanded to also includes up to this index to the left
                left_bound = bar[0]
                max_area = max(max_area, bar[1] * (i - bar[0]))

            # add new tuple which includes the height of the current bar along with
            # the index that it can go the farthest to the left for
            stack.append((left_bound, heights[i]))

        # Calculate the area for all the remainig heights in the stack
        # These rectangles were able to extend all the way to the end (len(heights) - 1)
        end = len(heights)
        while len(stack) != 0:
            remaining_bar = stack.pop()
            max_area = max(max_area, remaining_bar[1] * (end - remaining_bar[0]))

        return max_area

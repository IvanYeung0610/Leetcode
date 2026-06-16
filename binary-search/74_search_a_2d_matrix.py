"""
Ivan Yeung

74. Search a 2D Matrix
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # empty list edge case
        if not matrix or not matrix[0]:
            return False

        COLS = len(matrix[0])

        left = 0
        right = (len(matrix) * len(matrix[0])) - 1

        while left <= right:
            pivot = left + ((right - left) // 2)
            # convert single number to row & col index
            row = pivot // COLS
            col = pivot %  COLS

            if (matrix[row][col] < target):
                left = pivot + 1
            elif (matrix[row][col] > target):
                right = pivot - 1
            else: # target found
                return True

        return False

# NOTE: When getting the coordinates for the number, you need to divide and mod by the number of columns
# not the number of rows. This is because each row is built with the len(COLS) elements so you need to
# split it up that way.

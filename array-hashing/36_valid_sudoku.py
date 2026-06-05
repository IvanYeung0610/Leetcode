"""
Ivan Yeung

36. Valid Sudoku
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

    1. Each row must contain the digits 1-9 without repetition.
    2. Each column must contain the digits 1-9 without repetition.
    3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:

    A Sudoku board (partially filled) could be valid but is not necessarily solvable.
    Only the filled cells need to be validated according to the mentioned rules.

"""
from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows_count: dict[int, set[str]] = defaultdict(set)
        cols_count: dict[int, set[str]] = defaultdict(set)
        sqrs_count: dict[tuple[int, int], set[str]] = defaultdict(set)

        # iterate through the squares looking for dupes
        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in rows_count[row]:
                    return False
                elif board[row][col] in cols_count[col]:
                    return False
                elif board[row][col] in sqrs_count[((row//3), (col//3))]:
                    return False
                else:
                    rows_count[row].add(board[row][col])
                    cols_count[col].add(board[row][col])
                    sqrs_count[((row//3), (col//3))].add(board[row][col])

        return True


from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row: int):
            if row == n:
                board = ["".join(r) for r in current_board]
                result.append(board)
                return

            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue

                current_board[row][col] = 'Q'
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)

                current_board[row][col] = '.'
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        result = []
        cols = set()
        diag1 = set()
        diag2 = set()
        current_board = [['.'] * n for _ in range(n)]

        backtrack(0)
        return result

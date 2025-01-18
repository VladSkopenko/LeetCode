class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Solve the Sudoku puzzle in place using backtracking with optimization.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Precompute the sets and empty cells
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    empty_cells.append((r, c))
                else:
                    num = board[r][c]
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r // 3) * 3 + (c // 3)].add(num)

        def backtrack(index):
            if index == len(empty_cells):  # All empty cells are filled
                return True

            r, c = empty_cells[index]
            box_index = (r // 3) * 3 + (c // 3)

            for num in map(str, range(1, 10)):
                if num not in rows[r] and num not in cols[c] and num not in boxes[box_index]:
                    # Place the number
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[box_index].add(num)

                    # Recur for the next empty cell
                    if backtrack(index + 1):
                        return True

                    # Undo the placement (backtrack)
                    board[r][c] = '.'
                    rows[r].remove(num)
                    cols[c].remove(num)
                    boxes[box_index].remove(num)

            return False

        backtrack(0)

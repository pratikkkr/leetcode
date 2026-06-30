class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    empties.append((r, c))
                else:
                    b = (r // 3) * 3 + (c // 3)
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[b].add(val)

        def box_id(r, c):
            return (r // 3) * 3 + (c // 3)

        def backtrack(idx):
            if idx == len(empties):
                return True

            r, c = empties[idx]
            b = box_id(r, c)

            for d in '123456789':
                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    continue

                # place
                board[r][c] = d
                rows[r].add(d)
                cols[c].add(d)
                boxes[b].add(d)

                if backtrack(idx + 1):
                    return True

                # undo (backtrack)
                board[r][c] = '.'
                rows[r].remove(d)
                cols[c].remove(d)
                boxes[b].remove(d)

            return False

        backtrack(0)
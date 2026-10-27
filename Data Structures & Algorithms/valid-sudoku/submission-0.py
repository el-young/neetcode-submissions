class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col = [set() for _ in range(9)]
        row = [set() for _ in range(9)]
        box = [set() for _ in range(9)]
        for row_idx in range(9):
            for col_idx in range(9):
                
                digit = board[row_idx][col_idx]
                if digit == ".": continue

                box_idx = row_idx // 3 * 3 + col_idx // 3
                if digit in col[col_idx] or digit in row[row_idx] or digit in box[box_idx]:
                    return False

                col[col_idx].add(digit)
                row[row_idx].add(digit)
                box[box_idx].add(digit)
        return True

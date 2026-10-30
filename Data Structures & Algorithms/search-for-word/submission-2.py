class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW_DIM, COL_DIM = len(board), len(board[0])
        visited = set()

        def helper(rowIdx=-1, colIdx=-1, wIdx=0):
            if wIdx >= len(word): return True

            if rowIdx == -1:
                # Find starting if it exists
                for nxtRow in range(ROW_DIM):
                    for nxtCol in range(COL_DIM):
                        if board[nxtRow][nxtCol] == word[wIdx]:
                            visited.add((nxtRow, nxtCol))
                            if helper(nxtRow, nxtCol, wIdx + 1): return True
                            visited.remove((nxtRow, nxtCol))
            else:
                dirs = (
                    (rowIdx + 1, colIdx), 
                    (rowIdx - 1, colIdx), 
                    (rowIdx, colIdx + 1), 
                    (rowIdx, colIdx - 1)
                )
                for nxtRow, nxtCol in dirs:
                    if (not (0 <= nxtRow < ROW_DIM) or 
                        not (0 <= nxtCol < COL_DIM) or 
                        (nxtRow, nxtCol) in visited or
                        board[nxtRow][nxtCol] != word[wIdx]
                        ): 
                        continue
                    
                    visited.add((nxtRow, nxtCol))
                    if helper(nxtRow, nxtCol, wIdx + 1): return True
                    visited.remove((nxtRow, nxtCol))

            return False
        
        return helper()
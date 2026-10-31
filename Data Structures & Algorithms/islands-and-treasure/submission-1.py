from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF, DIRS = 2147483647, ((0, 1), (0, -1), (-1, 0), (1, 0))
        m, n = len(grid), len(grid[0])
        q = deque([])
        for rowIdx in range(m):
            for colIdx in range(n):
                if grid[rowIdx][colIdx] == 0: q.append((rowIdx, colIdx))
        
        depth = 1
        while q:
            for _ in range(len(q)):
                rowIdx, colIdx = q.popleft()
                for dy, dx in DIRS:
                    nxtRow, nxtCol = rowIdx + dy, colIdx + dx
                    if not 0 <= nxtRow < m: continue
                    if not 0 <= nxtCol < n: continue
                    if grid[nxtRow][nxtCol] != INF: continue
                    grid[nxtRow][nxtCol] = depth
                    q.append((nxtRow, nxtCol))
            depth += 1

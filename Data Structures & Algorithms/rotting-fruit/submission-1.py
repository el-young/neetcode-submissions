from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        DIRS, m, n = ((-1, 0), (1, 0), (0, -1), (0, 1)), len(grid), len(grid[0])
        countFresh = 0
        q = deque([])

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    countFresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c))
        
        if countFresh == 0: return 0

        time = 0
        while q:
            for _ in range(len(q)):
                # Spread rot
                r, c = q.popleft()
                for dy, dx in DIRS:
                    nxtR, nxtC = r + dy, c + dx
                    if not 0 <= nxtR < m or not 0 <= nxtC < n: 
                        continue
                    if grid[nxtR][nxtC] == 1:
                        countFresh -= 1
                        grid[nxtR][nxtC] = 2
                        q.append((nxtR, nxtC))
            time += 1

        return time - 1 if countFresh == 0 else -1


        
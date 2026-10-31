from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        
        def bfs(startNodes):
            valid = set(startNodes)
            q = deque(startNodes)

            while q:
                r, c = q.popleft()

                for nR, nC in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                    if not 0 <= nR < m: continue
                    if not 0 <= nC < n: continue
                    if (nR, nC) in valid: continue
                    if heights[nR][nC] >= heights[r][c]: 
                        valid.add((nR, nC))
                        q.append((nR, nC))
            
            return valid
        

        pacific = bfs([(r, 0) for r in range(m)] + [(0, c) for c in range(n)])
        atlantic = bfs([(r, n - 1) for r in range(m)] + [(m - 1, c) for c in range(n)])
        return [[r, c] for r in range(m) for c in range(n) if (r, c) in pacific and (r, c) in atlantic]
        
        



            
        
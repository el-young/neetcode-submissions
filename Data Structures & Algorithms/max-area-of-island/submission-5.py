class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = area = 0
        DIRS = ((0, 1), (0, -1), (-1, 0), (1, 0))

        def dfs(rowIdx, colIdx):
            nonlocal area
            area += 1
            grid[rowIdx][colIdx] = 0
            for dy, dx in DIRS:
                nxtRow, nxtCol = rowIdx + dy, colIdx + dx
                if not 0 <= nxtRow < len(grid): continue
                if not 0 <= nxtCol < len(grid[0]): continue
                if not grid[nxtRow][nxtCol]: continue
                dfs(nxtRow, nxtCol)
        
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                if grid[rowIdx][colIdx]:
                    area = 0
                    dfs(rowIdx, colIdx)
                    maxArea = max(maxArea, area)
        
        return maxArea
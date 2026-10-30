class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        DIRS = (
            (1, 0),
            (-1, 0),
            (0, -1),
            (0, 1),
        )
        visited = set()
        def dfs(rowIdx, colIdx):
                visited.add((rowIdx, colIdx))
                for dy, dx in DIRS:
                    if (rowIdx + dy, colIdx + dx) in visited: continue
                    if not 0 <= rowIdx + dy < len(grid): continue
                    if not 0 <= colIdx + dx < len(grid[0]): continue
                    if grid[rowIdx + dy][colIdx + dx] == "0": continue
                    dfs(rowIdx + dy, colIdx + dx)
                
        islands = 0
        for rowIdx in range(len(grid)):
            for colIdx in range(len(grid[0])):
                if (rowIdx, colIdx) not in visited and grid[rowIdx][colIdx] == "1":
                    islands += 1
                    dfs(rowIdx, colIdx)
        
        return islands
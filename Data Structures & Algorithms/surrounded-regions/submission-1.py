class Solution:
    def solve(self, board: List[List[str]]) -> None:
        n, m = len(board), len(board[0])

        reachable = set()
        def dfs(r, c):
            for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
                if not 0 <= nr < n or not 0 <= nc < m: continue
                if (nr, nc) not in reachable and board[nr][nc] == "O": 
                    reachable.add((nr, nc))
                    dfs(nr, nc)
        
        for r in range(n): 
            if board[r][0] == "O": dfs(r, 0)
            if board[r][m - 1] == "O": dfs(r, m - 1)
        
        for c in range(m):
            if board[0][c] == "O": dfs(0, c)
            if board[n - 1][c] == "O": dfs(n - 1, c)

        for r in range(1, n - 1):
            for c in range(1, m - 1):
                if board[r][c] == "O" and (r, c) not in reachable:
                    board[r][c] = "X"
        
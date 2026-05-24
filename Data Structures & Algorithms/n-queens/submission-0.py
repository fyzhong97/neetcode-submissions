class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [['.'] * n for _ in range(n)]

        cols = set()
        diag1 = set()  # r - c
        diag2 = set()  # r + c

        def dfs(r):
            
            if r == n:
                res.append(["".join(x) for x in board])
                return
            
            # decide which column to pick
            for c in range(n):
                
                if (r + c in diag2) or (r - c in diag1) or c in cols:
                    continue
                
                cols.add(c)
                diag1.add(r-c)
                diag2.add(r+c)
                board[r][c] = 'Q'
                dfs(r + 1)

                cols.remove(c)
                diag1.remove(r-c)
                diag2.remove(r+c)
                board[r][c] = '.'
                
        dfs(0)

        return res
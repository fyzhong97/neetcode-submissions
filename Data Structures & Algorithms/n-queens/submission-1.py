class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col, d1, d2 = set(), set(), set()
        res = []
        board = [['.'] * n for _ in range(n)]
        def dfs(r):
            
            if r == n:
                res.append(["".join(x) for x in board])
                return
            
            for c in range(n):
                
                if c in col or (r + c in d1) or (r - c in d2):
                    continue
                
                board[r][c] = 'Q'
                col.add(c)
                d1.add(r + c)
                d2.add(r - c)
                
                dfs(r + 1)
                
                board[r][c] = '.'
                col.remove(c)
                d1.remove(r + c)
                d2.remove(r - c)

        dfs(0)
        return res
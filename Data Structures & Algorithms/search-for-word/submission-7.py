class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(word)
        h, w = len(board), len(board[0])
        moves = [(0,1), (0,-1), (1,0), (-1,0)]

        def dfs(r,c,idx,curpath, visited):
            
            if board[r][c] != word[idx]:
                return False
            
            # now the stuff are equal
            visited[r][c] = True
            curpath.append(board[r][c])

            if len(curpath) == n:
                return True

            for mov in moves:
                
                nr, nc = r + mov[0], c + mov[1]
                if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                    if dfs(nr,nc,idx+1,curpath,visited):
                        return True

            visited[r][c] = False
            curpath.pop()

        for r in range(h):
            for c in range(w):
                visited = [[False] * w for _ in range(h)]
                if dfs(r, c, 0, [], visited):
                    return True

        return False

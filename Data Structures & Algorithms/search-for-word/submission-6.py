class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        n = len(word)
        h, w = len(board), len(board[0])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(r, c, idx, visited):
            if board[r][c] != word[idx]:
                return False

            if idx == n - 1:
                return True

            visited[r][c] = True

            for dr, dc in moves:
                nr, nc = r + dr, c + dc

                if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc]:
                    if dfs(nr, nc, idx + 1, visited):
                        return True

            visited[r][c] = False
            return False

        for r in range(h):
            for c in range(w):
                if board[r][c] == word[0]:
                    visited = [[False] * w for _ in range(h)]
                    if dfs(r, c, 0, visited):
                        return True

        return False
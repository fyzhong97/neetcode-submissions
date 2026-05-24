class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        h, w = len(grid), len(grid[0])
        q = deque()
        moves = [(0,1), (0,-1), (1,0), (-1,0)]

        for r in range(h):
            for c in range(w):
                if grid[r][c] == 0:
                    q.append((r, c))

        while q:
            r,c = q.popleft()
            
            for dr, dc in moves:
                nr, nc = r + dr, c + dc

                if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 2147483647:
                    grid[nr][nc] = grid[r][c] + 1
                    q.append((nr,nc))
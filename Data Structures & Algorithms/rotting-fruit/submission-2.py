from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h, w = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        moves = [(0,1), (0,-1), (1,0), (-1,0)]

        for r in range(h):
            for c in range(w):
                if grid[r][c] == 2:
                    q.append([r,c])
                elif grid[r][c] == 1:
                    fresh += 1
        
        minutes = 0
        
        while q and fresh > 0:
            for _ in range(len(q)):
                r,c = q.popleft()
                for dr, dc in moves:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        q.append([nr,nc])
                        fresh -= 1
            minutes += 1
        
        if fresh != 0:
            return -1

        return minutes
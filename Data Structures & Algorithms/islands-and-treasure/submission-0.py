from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        h, w = len(grid), len(grid[0])
        res = [[2147483647] * w for _ in range(h)]
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        def bfs(r, c):

            visited = [[False] * w for _ in range(h)]
            node = deque([(r,c)])
            visited[r][c] = True
            dist = 0

            while node:

                for _ in range(len(node)):
                    
                    curnode = node.popleft()
                    r,c = curnode[0], curnode[1]

                    for i,mov in enumerate(moves):
                        nr, nc = r+mov[0], c+mov[1]
                        if 0 <= nr < h and 0 <= nc < w and not visited[nr][nc] and grid[nr][nc] != -1:
                            node.append((nr,nc))
                            visited[nr][nc] = True

                            if grid[nr][nc] == 0:
                                return dist + 1
                dist += 1

            return 2147483647
            
        for r in range(h):
            for c in range(w):
                if grid[r][c] == 2147483647:
                    res[r][c] = bfs(r,c)
                else:
                    res[r][c] = grid[r][c]
        for r in range(h):
            for c in range(w):
                grid[r][c] = res[r][c]
    
                        
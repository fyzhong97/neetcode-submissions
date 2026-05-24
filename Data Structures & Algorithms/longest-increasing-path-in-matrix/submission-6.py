from functools import cache
import sys

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        sys.setrecursionlimit(10**6)

        h, w = len(matrix), len(matrix[0])
        moves = [(0,1),(0,-1),(1,0),(-1,0)]
        
        @cache
        def dfs(r, c):
            goodpathlen = 0

            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < h and 0 <= nc < w and matrix[nr][nc] > matrix[r][c]:
                    goodpathlen = max(goodpathlen, dfs(nr, nc))
            
            return 1 + goodpathlen
        
        return max(dfs(r, c) for r in range(h) for c in range(w))
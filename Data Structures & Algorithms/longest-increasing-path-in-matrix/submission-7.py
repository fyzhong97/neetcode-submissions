class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        mem = [[None for _ in row] for row in matrix]

        def dfs(matrix, i, j, mem):
            if mem[i][j] is not None:
                return mem[i][j]

            res = 1
            if i > 0 and matrix[i - 1][j] > matrix[i][j]:
                res = max(res, 1 + dfs(matrix, i - 1, j, mem))
            if i < len(matrix) - 1 and matrix[i + 1][j] > matrix[i][j]:
                res = max(res, 1 + dfs(matrix, i + 1, j, mem))
            if j > 0 and matrix[i][j - 1] > matrix[i][j]:
                res = max(res, 1 + dfs(matrix, i, j - 1, mem))
            if j < len(matrix[i]) - 1 and matrix[i][j + 1] > matrix[i][j]:
                res = max(res, 1 + dfs(matrix, i, j + 1, mem))
            mem[i][j] = res

            return res

        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                res = max(res, dfs(matrix, i, j, mem))

        return res

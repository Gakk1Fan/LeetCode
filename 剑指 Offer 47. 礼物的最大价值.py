class Solution:
    def maxValue(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        f = [[0] * (cols + 1) for _ in range(rows + 1)]
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                f[i][j] = max(f[i-1][j], f[i][j-1]) + grid[i-1][j-1]
        return f[rows][cols]
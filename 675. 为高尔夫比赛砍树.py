class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        n, m = len(forest), len(forest[0])
        def bfs(sx, sy, ex, ey):
            #  n * m行矩阵， 记录(sx, sy)到当前坐标的最短距离
            d = [[-1] * m for _ in range(n)]

            # BFS一般步骤
            q = collections.deque()
            q.append((sx, sy))
            # 初始化起始距离
            d[sx][sy] = 0
            while q:
                x, y = q.popleft()
                if x == ex and y == ey:
                    return d[x][y]
                for a, b in (x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1):
                    if a < 0 or a >= n or b < 0 or b >= m:
                        continue
                    if d[a][b] == -1 and forest[a][b] > 0:
                        d[a][b] = d[x][y] + 1
                        q.append((a, b))
            return -1
        
        trs = sorted((forest[i][j], i, j) for i, j in product(range(n), range(m)) if forest[i][j] > 1)
        x, y, ans = 0, 0, 0
        for (c, a, b) in trs:
            e = bfs(x, y, a, b)
            x, y = a, b
            if e == -1:
                return -1
            ans += e
        return ans

"""
    多次BFS，每次都求从当前最矮的树到次矮的树的最小距离
    时间复杂度O(n^2 * m^2)
"""
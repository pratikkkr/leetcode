from collections import deque

class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])

        # If even the safest possible path can't keep us alive, no point searching
        INF = float('inf')
        cost = [[INF] * n for _ in range(m)]
        cost[0][0] = grid[0][0]

        dq = deque([(0, 0)])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while dq:
            r, c = dq.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n:
                    new_cost = cost[r][c] + grid[nr][nc]
                    if new_cost < cost[nr][nc]:
                        cost[nr][nc] = new_cost
                        if grid[nr][nc] == 0:
                            dq.appendleft((nr, nc))
                        else:
                            dq.append((nr, nc))

        return health - cost[m - 1][n - 1] >= 1
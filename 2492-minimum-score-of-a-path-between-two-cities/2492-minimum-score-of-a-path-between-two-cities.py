class Solution:
    def minScore(self, n: int, roads: list[list[int]]) -> int:
        parent = list(range(n + 1))
        rank = [0] * (n + 1)

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]  # path compression
                x = parent[x]
            return x

        def union(x: int, y: int) -> None:
            rx, ry = find(x), find(y)
            if rx == ry:
                return
            if rank[rx] < rank[ry]:
                rx, ry = ry, rx
            parent[ry] = rx
            if rank[rx] == rank[ry]:
                rank[rx] += 1

        for a, b, _ in roads:
            union(a, b)

        min_dist = [float('inf')] * (n + 1)
        for a, b, dist in roads:
            root = find(a)
            min_dist[root] = min(min_dist[root], dist)

        return min_dist[find(1)]
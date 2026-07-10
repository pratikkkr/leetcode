from typing import List

class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 1. sort node indices by value
        order = sorted(range(n), key=lambda i: nums[i])
        val = [nums[i] for i in order]
        pos = [0] * n
        for sp, orig in enumerate(order):
            pos[orig] = sp

        # 2. two-pointer: R[i] = farthest sorted index directly reachable from i
        R = [0] * n
        j = 0
        for i in range(n):
            if j < i:
                j = i
            while j + 1 < n and val[j + 1] - val[i] <= maxDiff:
                j += 1
            R[i] = j

        # 3. connected components via merge-interval sweep
        comp = [0] * n
        comp_id = 0
        max_reach = R[0]
        comp[0] = 0
        for i in range(1, n):
            if i > max_reach:
                comp_id += 1
            comp[i] = comp_id
            if R[i] > max_reach:
                max_reach = R[i]

        # 4. binary lifting table
        LOG = max(1, n.bit_length())
        up = [R[:]]
        for k in range(1, LOG):
            prev = up[k - 1]
            up.append([prev[prev[i]] for i in range(n)])

        # 5. answer queries
        ans = []
        for u, v in queries:
            pu, pv = pos[u], pos[v]
            if pu == pv:
                ans.append(0)
                continue
            if comp[pu] != comp[pv]:
                ans.append(-1)
                continue
            p, q = (pu, pv) if pu < pv else (pv, pu)
            cur = p
            steps = 0
            for k in range(LOG - 1, -1, -1):
                nxt = up[k][cur]
                if nxt < q:
                    cur = nxt
                    steps += (1 << k)
            steps += 1
            ans.append(steps)

        return ans
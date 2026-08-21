class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)

        # Precompute (lcm, parity) for every non-empty subset
        subsets = []
        for mask in range(1, 1 << n):
            l = 1
            bits = 0
            for i in range(n):
                if mask & (1 << i):
                    l = l * coins[i] // gcd(l, coins[i])
                    bits += 1
            subsets.append((l, bits))

        def count(m: int) -> int:
            total = 0
            for l, bits in subsets:
                total += (m // l) if bits % 2 == 1 else -(m // l)
            return total

        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
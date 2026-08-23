class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        diff = 0          # sum(left known) - sum(right known)
        leftQ = rightQ = 0

        for i in range(half):
            if num[i] == '?':
                leftQ += 1
            else:
                diff += int(num[i])

        for i in range(half, n):
            if num[i] == '?':
                rightQ += 1
            else:
                diff -= int(num[i])

        q = leftQ + rightQ
        if q % 2 == 1:
            return True  # Alice always wins with an odd number of '?'

        diff_final = diff + 9 * (leftQ - rightQ) // 2
        return diff_final != 0
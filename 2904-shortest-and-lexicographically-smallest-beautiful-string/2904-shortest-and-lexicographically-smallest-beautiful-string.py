class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        best = ""
        left = 0
        ones = 0

        for right in range(n):
            if s[right] == '1':
                ones += 1

            # Shrink: drop extra 1s and any leading 0s
            while ones > k or (left <= right and s[left] == '0'):
                if s[left] == '1':
                    ones -= 1
                left += 1

            if ones == k:
                window = s[left:right + 1]
                if (not best
                    or len(window) < len(best)
                    or (len(window) == len(best) and window < best)):
                    best = window

        return best
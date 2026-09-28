class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0] * n
        stack = []

        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            elif ch == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        res = []
        i, d = 0, 1
        while i < n:
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d

        return ''.join(res)
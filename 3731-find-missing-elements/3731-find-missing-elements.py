class Solution:
    def findMissingElements(self, nums: list[int]) -> list[int]:
        num_set = set(nums)
        lo, hi = min(nums), max(nums)

        missing = []
        for x in range(lo, hi + 1):
            if x not in num_set:
                missing.append(x)

        return missing
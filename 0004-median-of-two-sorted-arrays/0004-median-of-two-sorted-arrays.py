class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            cut1 = (left + right) // 2
            cut2 = (m + n + 1)//2 - cut1
            
            L1 = float('-inf') if cut1 == 0 else nums1[cut1-1]
            R1 = float('inf')  if cut1 == m else nums1[cut1]
            
            L2 = float('-inf') if cut2 == 0 else nums2[cut2-1]
            R2 = float('inf')  if cut2 == n else nums2[cut2]
            
            if L1 <= R2 and L2 <= R1:
                if (m+n) % 2 == 0:
                    return (max(L1, L2) + min(R1, R2)) / 2
                else:
                    return max(L1, L2)
            
            elif L1 > R2:
                right = cut1 - 1
            else:
                left = cut1 + 1
class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set1 = set(nums1)
        result = []
        
        for num in nums2:
            if num in set1:
                result.append(num)
                
        return list(set(result))

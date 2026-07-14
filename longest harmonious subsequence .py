from collections import Counter

class Solution:
    def findLHS(self, nums: list[int]) -> int:
        num_counts = Counter(nums)
        max_length = 0
        
        for num in num_counts:
            if num + 1 in num_counts:
                current_length = num_counts[num] + num_counts[num + 1]
                if current_length > max_length:
                    max_length = current_length
                    
        return max_length

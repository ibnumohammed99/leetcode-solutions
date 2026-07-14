class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        max_len = 0
        n = len(nums)
        for i in range(n):
            if nums [i] % 2 == 0 and nums[i] <= threshold:
                j = i
                while j + 1 < n and nums[j+1] <= threshold and (nums[j] % 2 != nums[j+1] % 2):
                    j += 1
                current_len = j - i + 1
                if current_len > max_len:
                    max_len = current_len 
        return max_len
   

class Solution:
    def countDigitOccurrences(self, nums: List[int], digit: int) -> int:
        total_count = 0
        digit_str = str(digit)
        
        for num in nums:
            total_count += str(num).count(digit_str)
            
        return total_count

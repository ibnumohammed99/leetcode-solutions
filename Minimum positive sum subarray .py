class Solution:
    def minimumSumSubarray(self, nums, l, r):
        answer = float('inf')

        for start in range(len(nums)):
            total = 0

            for end in range(start, len(nums)):
                total += nums[end]

                length = end - start + 1

                if length >= l and length <= r:
                    if total > 0:
                        answer = min(answer, total)

                if length > r:
                    break

        if answer == float('inf'):
            return -1

        return answer

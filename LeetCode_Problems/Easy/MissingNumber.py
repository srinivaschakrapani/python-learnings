from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        arrsum = 0
        for i in nums:
            arrsum += i
        n = len(nums)
        totalSum = int(n * (n + 1) / 2)
        return totalSum - arrsum
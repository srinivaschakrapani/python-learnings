from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        index = 0
        leftsum = 0
        totalsum = 0
        for i in nums:
            totalsum += i

        while index < len(nums):
            rightsum = totalsum - nums[index] - leftsum
            if leftsum == rightsum:
                return index
            else:
                leftsum = leftsum + nums[index]
                index += 1
        return -1
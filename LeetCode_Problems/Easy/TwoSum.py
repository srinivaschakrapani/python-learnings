# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            diff = (target - nums[i])
            if diff in nums:
                t_index = nums.index(diff)
                if i != t_index:
                    return [i, nums.index(diff)]
                continue


s = Solution()
inp = [3, 2, 4]
target = 6
print(s.twoSum(inp, target))

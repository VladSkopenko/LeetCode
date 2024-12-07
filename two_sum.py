"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order."""

from typing import List


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        num_to_index = {}
        for i, num in enumerate(nums):
            num_to_index[num] = i
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution.twoSum(nums, target))

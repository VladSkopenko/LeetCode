"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.
Return the sum of the three integers.
"""
from typing import List


class Solution:
    @staticmethod
    def three_sum_closest(nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for index in range(len(nums)):
            left = index + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[index] + nums[left] + nums[right]
                if abs(target - current_sum) < abs(target - closest_sum):
                    closest_sum = current_sum
                if current_sum < target:
                    left += 1
                elif current_sum > target:
                    right -= 1
                else:
                    return current_sum
        return closest_sum

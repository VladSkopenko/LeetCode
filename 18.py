"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""

from typing import List


class Solution:
    def four_sum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result = []
        len_nums = len(nums)
        for first_index in range(len_nums - 3):
            if first_index > 0 and nums[first_index] == nums[first_index - 1]:
                continue
            for second_index in range(first_index + 1, len_nums - 2):
                if (
                    second_index > first_index + 1
                    and nums[second_index] == nums[second_index - 1]
                ):
                    continue
                left = second_index + 1
                right = len_nums - 1
                while left < right:
                    current_sum = (
                        nums[first_index]
                        + nums[second_index]
                        + nums[left]
                        + nums[right]
                    )
                    if target == current_sum:
                        r = [
                            nums[first_index],
                            nums[second_index],
                            nums[left],
                            nums[right],
                        ]
                        result.append(r)
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    if current_sum > target:
                        right -= 1
                    elif current_sum < target:
                        left += 1

        return result

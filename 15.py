"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
from typing import List


class Solution:
    def three_sum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        r = []
        for index, element in enumerate(nums):
            if index > 0 and element == nums[index - 1]:
                continue
            left = index + 1
            right = len(nums) - 1
            while left < right:
                result = element + nums[right] + nums[left]
                if result == 0:
                    result = [element, nums[right], nums[left]]
                    r.append(result)
                    right -= 1
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif result > 0:
                    right -= 1
                else:
                    left += 1

        return r


if __name__ == "__main__":
    n = [-1, 0, 1, 2, -1, -4]
    print(Solution().three_sum(n))

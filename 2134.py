from typing import List

input_list = [0, 1, 0, 1, 1, 0, 0]


class Solution:
    @classmethod
    def minSwaps(cls, nums: List[int]) -> int:
        total = nums.count(1)
        n = len(nums)
        circle_array = nums + nums
        current_zeros = total - sum(nums[:total])
        min_swaps = current_zeros
        for i in range(1, n):
            if circle_array[i - 1] == 0:
                current_zeros -= 1
            if circle_array[i + total - 1] == 0:
                current_zeros += 1
            min_swaps = min(min_swaps, current_zeros)
        return min_swaps


print(Solution.minSwaps(input_list))

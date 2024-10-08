from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        MOD = 10**9 + 7
        subarray_sums = []
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                subarray_sums.append(current_sum)
        subarray_sums.sort()
        result = 0
        for i in range(left - 1, right):
            result = (result + subarray_sums[i]) % MOD

        return result

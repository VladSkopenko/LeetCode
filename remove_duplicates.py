"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k."""
from typing import List


class Solution:
    @staticmethod
    def removeDuplicates(nums: List[int]) -> int:
        if not nums:
            return 0

        k = 1

        for i in range(1, len(nums)):  # i = 1
            if nums[i] != nums[i - 1]: # Проверяю уникальный или нет
                nums[k] = nums[i] # Перезаписываю уникальные в начало
                k += 1

        return k


s = Solution()
a = [1, 1, 1, 2, 2, 3, 4, 4, 5, 5, 6]
print(s.removeDuplicates(a))

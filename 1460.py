"""
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray
of arr and reverse it. You are allowed to make any number of steps.
Return true if you can make arr equal to target or false otherwise
"""

from typing import List


class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for element in target:
            if element in arr:
                arr.remove(element)
        if len(arr) == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    print(Solution().canBeEqual(target, arr))

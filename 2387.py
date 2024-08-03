from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        ls = nums1 + nums2
        ls.sort()
        n = len(ls)
        if n % 2 == 1:
            result = ls[n // 2]
        else:
            mid1 = n // 2 - 1
            mid2 = n // 2
            result = (ls[mid1] + ls[mid2]) / 2.0
        return result


if __name__ == "__main__":
    print(Solution.findMedianSortedArrays([1, 3], [2, 3]))

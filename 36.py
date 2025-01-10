from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    result = mid
                    if is_first:
                        right = mid - 1
                    else:
                        left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result
        first_position = find_bound(True)
        last_position = find_bound(False)

        return [first_position, last_position]

"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""
from typing import List


class Solution:
    @classmethod
    def longestCommonPrefix(cls, strs: List[str]) -> str:
        if not strs:
            return ""
        min_str_in_strs = min(strs, key=len)
        for index in range(len(min_str_in_strs)):
            for string in strs:
                if string[index] != min_str_in_strs[index]:
                    return min_str_in_strs[:index]
        return min_str_in_strs


if __name__ == "__main__":
    lst = ["flower", "flow", "flight"]
    print(Solution.longestCommonPrefix(lst))

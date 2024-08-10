"""
Given a string s, find the length of the longest
substring without repeating characters.
"""

s1 = "abcabcbb"


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        dict_c = {}
        for i in range(n):
            if s[i] in dict_c:
                dict_c[s[i]] = i
                if i - dict_c[s[i]] > dict_c[s[i]]:
                    dict_c[s[i]] = i

            else:
                dict_c[s[i]] = i
        result = len(dict_c)

        return result


if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring(s1))

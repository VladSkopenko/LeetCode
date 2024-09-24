"""
Given a string s, find the length of the longest
substring without repeating characters.
"""

s1 = "abcabcbb"


class Solution:
    def length_of_longest_substring(self, s: str) -> int:
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
    print(Solution().length_of_longest_substring(s1))

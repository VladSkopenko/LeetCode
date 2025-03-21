"""1653. Minimum Deletions to Make String Balanced
Medium
Topics
Companies
Hint
You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.
"""


class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_right = s.count("a")
        b_left = 0

        min_deletions = a_right

        for c in s:
            if c == "a":
                a_right -= 1
            else:  # c == 'b'
                b_left += 1

            min_deletions = min(min_deletions, a_right + b_left)

        return min_deletions


a = "aaabbba"
s = Solution()
print(s.minimumDeletions(a))

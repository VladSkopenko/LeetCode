"""
Given a string s, return the longest
palindromic substring in s."""


class Solution:
    def longest_palindrome(self, s: str) -> str:
        if not s:
            return ""

        def expandAroundCenter(left: int, right: int) -> str:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1 : right]

        longest = ""
        for i in range(len(s)):
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(longest):
                longest = odd_palindrome

            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(longest):
                longest = even_palindrome

        return longest

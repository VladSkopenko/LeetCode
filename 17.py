"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
"""

from typing import List


class Solution:
    def letter_combinations(self, digits: str) -> List[str]:
        result = []
        dict_n = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        if not digits:
            return []

        def backtrack(index, current_combination):
            if index == len(digits):
                result.append(current_combination)
                return
            current_digit = digits[index]
            possible_letters = dict_n[current_digit]

            for letter in possible_letters:
                backtrack(index + 1, current_combination + letter)

        result = []
        backtrack(0, "")
        return result

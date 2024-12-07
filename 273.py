"""
273. Integer to English Words
Convert a non-negative integer num to its English words representation.
"""

import re


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        def one(num):
            switcher = {
                1: "One",
                2: "Two",
                3: "Three",
                4: "Four",
                5: "Five",
                6: "Six",
                7: "Seven",
                8: "Eight",
                9: "Nine",
                10: "Ten",
                11: "Eleven",
                12: "Twelve",
                13: "Thirteen",
                14: "Fourteen",
                15: "Fifteen",
                16: "Sixteen",
                17: "Seventeen",
                18: "Eighteen",
                19: "Nineteen",
            }
            return switcher.get(num, "")

        def tens(num):
            switcher = {
                2: "Twenty",
                3: "Thirty",
                4: "Forty",
                5: "Fifty",
                6: "Sixty",
                7: "Seventy",
                8: "Eighty",
                9: "Ninety",
            }
            ten, remainder = divmod(num, 10)
            if ten == 1:
                return one(num)  # Special case for numbers between 10 and 19
            return switcher.get(ten, "") + (" " + one(remainder) if remainder else "")

        def less_than_thousand(num):
            hundred, remainder = divmod(num, 100)
            result = []
            if hundred:
                result.append(one(hundred) + " Hundred")
            if remainder:
                result.append(tens(remainder))
            return " ".join(result)

        billion, remainder = divmod(num, 1_000_000_000)
        million, remainder = divmod(remainder, 1_000_000)
        thousand, remainder = divmod(remainder, 1_000)

        result = []
        if billion:
            result.append(less_than_thousand(billion) + " Billion")
        if million:
            result.append(less_than_thousand(million) + " Million")
        if thousand:
            result.append(less_than_thousand(thousand) + " Thousand")
        if remainder:
            result.append(less_than_thousand(remainder))
        r = " ".join(result).strip()
        r = re.sub(r"\s+", " ", r)

        return r


if __name__ == "__main__":
    print(Solution().numberToWords(123))
    print(Solution().numberToWords(1234567891))

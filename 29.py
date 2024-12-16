"""
Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""


class Solution:
    @staticmethod
    def divide(dividend: int, divisor: int) -> int:
        if dividend == -(2 ** 31) and divisor == -1:
            return 2 ** 31 - 1
        sign = (dividend > 0) != (divisor > 0)
        count = 0
        dividend, divisor = abs(dividend), abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            count += 1
        return count if not sign else -count


if __name__ == "__main__":
    print(Solution.divide(10, 3))
    print(Solution.divide(7, -3))

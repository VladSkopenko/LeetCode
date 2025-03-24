"""
50. Pow(x, n)
Medium
Topics
Companies
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
"""


class Solution:
    def my_pow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            x = 1 / x
            n = -n

        result = 1
        while n > 0:
            if n % 2 == 1:
                result *= x
            x *= x
            n //= 2

        return result
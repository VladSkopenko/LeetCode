"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
 the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1

        reversed_x = int(str(abs(x))[::-1])

        reversed_x *= sign

        if reversed_x < - 2 ** 31 or reversed_x > 2 ** 31 - 1:
            return 0

        return reversed_x


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))
    print(s.reverse(1534236469))

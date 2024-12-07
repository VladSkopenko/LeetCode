"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M."""


class Solution:
    @classmethod
    def romanToInt(cls, s: str) -> int:
        data = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        result = 0
        prev_value = 0

        for num in s:
            current_value = data[num]
            if current_value > prev_value:
                result += current_value - 2 * prev_value
            else:
                result += current_value
            prev_value = current_value

        return result


if __name__ == "__main__":
    print(Solution.romanToInt("III"))
    print(Solution.romanToInt("IV"))
    print(Solution.romanToInt("IX"))
    print(Solution.romanToInt("LVIII"))
    print(Solution.romanToInt("MCMXCIV"))

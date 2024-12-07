class Solution:
    def myAtoi(self, s: str) -> int:
        # Шаг 1: Игнорируем начальные пробелы
        s = s.lstrip()
        if not s:
            return 0

        # Шаг 2: Определение знака числа
        sign = 1
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            s = s[1:]

        # Шаг 3: Преобразование строки в число
        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        # Шаг 4: Применение знака
        result *= sign

        # Шаг 5: Ограничение в пределах 32-битного целого числа
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX

        return result

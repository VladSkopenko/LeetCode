"""Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in
$1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.
Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day."""


class Solution:
    @staticmethod
    def totalMoney(n: int) -> int:
        result = 0
        start = 1  # сумма, которую кладут в понедельник
        current = 0  # текущая сумма на данный день недели

        for day in range(1, n + 1):
            if day % 7 == 1:  # если это понедельник
                current = start
                start += 1  # следующий понедельник будет на 1 больше
            else:
                current += 1

            result += current

        return result
    
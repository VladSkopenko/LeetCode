'''There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).'''
from typing import List

rating1 = [2, 5, 3, 4, 1]  # 3
rating2 = [2, 1, 3]  # 0
rating3 = [1, 2, 3, 4]  # 4


class Solution:
    @staticmethod
    def numTeams(rating: List[int]) -> int:
        n = len(rating)
        count = 0

        for j in range(1, n - 1):
            left_less = left_more = right_less = right_more = 0

            for i in range(j):
                if rating[i] < rating[j]: 
                    left_less += 1
                if rating[i] > rating[j]:
                    left_more += 1

            for k in range(j + 1, n):
                if rating[k] < rating[j]:
                    right_less += 1
                if rating[k] > rating[j]:
                    right_more += 1

            count += left_less * right_more + left_more * right_less

        return count


# Пример работы алгоритма:
# Проходим по каждому элементу как по среднему элементу j:
# j = 1, rating[j] = 5:
#   Элементы слева: [2]
#   Элементы справа: [3, 4, 1]
#   left_less = 1 (rating[0] < rating[1])
#   right_less = 2 (rating[2] < rating[1], rating[4] < rating[1])
#   right_more = 1 (rating[3] > rating[1])
#   Количество команд: 1 * 2 + 0 * 1 = 2

# j = 2, rating[j] = 3:
#   Элементы слева: [2, 5]
#   Элементы справа: [4, 1]
#   left_less = 1 (rating[0] < rating[2])
#   left_more = 1 (rating[1] > rating[2])
#   right_less = 1 (rating[4] < rating[2])
#   right_more = 1 (rating[3] > rating[2])
#   Количество команд: 1 * 1 + 1 * 1 = 2

# j = 3, rating[j] = 4:
#   Элементы слева: [2, 5, 3]
#   Элементы справа: [1]
#   left_less = 2 (rating[0] < rating[3], rating[2] < rating[3])
#   left_more = 1 (rating[1] > rating[3])
#   right_less = 1 (rating[4] < rating[3])
#   Количество команд: 2 * 1 + 1 * 1 = 3

# Общее количество команд: 2 + 2 + 3 = 7

# Однако на самом деле команда с элементами rating[1], rating[2], rating[3] не является валидной,
# поэтому общее количество валидных команд: 3 (rating[0], rating[2], rating[3], rating[0], rating[3], rating[4], rating[2], rating[3], rating[4])
if __name__ == '__main__':
    s = Solution()
    print(s.numTeams(rating1))
    print(s.numTeams(rating2))
    print(s.numTeams(rating3))
    a = range(5) # 0-4


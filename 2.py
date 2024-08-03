from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()  # Вспомогательный узел
        current = dummy  # Указатель для текущего узла
        carry = 0  # Переменная для хранения переноса

        # Пока есть узлы в любом из списков или есть перенос
        while l1 or l2 or carry:
            # Получаем значения текущих узлов, если они есть
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            # Вычисляем сумму и перенос
            total = val1 + val2 + carry
            carry = total // 10  # Перенос
            digit = total % 10  # Остаток

            # Создаем новый узел для результата
            current.next = ListNode(digit)
            current = current.next

            # Передвигаемся к следующему узлу в списках
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next





l1 = [2, 4, 3]
l2 = [5, 6, 4]
п

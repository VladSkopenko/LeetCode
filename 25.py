from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse_linked_list(start: ListNode, end: ListNode) -> ListNode:
            """Переворачивает узлы в списке от start до end (не включая end)."""
            prev, current = None, start
            while current != end:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy

        while length >= k:
            group_start = prev_group_end.next
            group_end = group_start
            for _ in range(k):
                group_end = group_end.next


            new_start = reverse_linked_list(group_start, group_end)

            prev_group_end.next = new_start
            group_start.next = group_end


            prev_group_end = group_start
            length -= k

        return dummy.next
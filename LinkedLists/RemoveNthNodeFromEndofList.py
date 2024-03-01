class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        while n > 0 and p1:
            p1 = p1.next
            n -= 1

        dummy = ListNode(None, head)
        p2 = dummy
        while p1:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next

        return dummy.next
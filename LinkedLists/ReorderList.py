# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # 1) find the mid point

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # 2) split down the middle
        l1 = head
        l2 = mid



        # 3) Reverse the second portion

        prev = None
        curr = l2
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        l2 = prev

        # 4) Merge the two lists in an alternating order
        while l1 and l2:

            tmp1 = l1.next
            tmp2 = l2.next

            l1.next = l2
            l2.next = tmp1
            l1 = tmp1
            l2 = tmp2


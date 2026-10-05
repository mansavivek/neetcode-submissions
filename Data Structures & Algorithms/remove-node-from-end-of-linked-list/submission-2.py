# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        first = head
        second = dummy
        # count = 0
        while n>0 :
            first = first.next
            n = n-1
        print(count)
        if count == 1 and n == 1:
            return head.next
        while first:
            first= first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for lst in lists:
            while lst:
                arr.append(lst.val)
                lst=lst.next
        arr.sort()

        res = ListNode(0)
        cur = res
        for i in arr:
            cur.next = ListNode(i)
            cur = cur.next
        return res.next
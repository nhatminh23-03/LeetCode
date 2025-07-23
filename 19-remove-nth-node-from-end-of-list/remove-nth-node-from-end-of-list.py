# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l, r = head, head
        while r and n > 0:
            r = r.next
            n -= 1 
        
        if r is None:
            return head.next
        
        while r and r.next:
            l = l.next
            r = r.next
        
        l.next = l.next.next

        return head
        
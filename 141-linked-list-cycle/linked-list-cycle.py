# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # setList = set()
        # curr = head 
        # while curr:
        #     if curr in setList:
        #         return True 
        #     setList.add(curr)
        #     curr = curr.next
        # return False
        slow, fast = head, head 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
            if slow == fast:
                return True
        return False

        
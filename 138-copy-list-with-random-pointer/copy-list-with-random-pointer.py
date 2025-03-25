"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dictNode = { None: None}

        curr = head 
        while curr:
            copy = Node(curr.val)
            dictNode[curr] = copy
            curr = curr.next 
        
        curr = head
        while curr:
            copy = dictNode[curr]
            copy.next = dictNode[curr.next]
            copy.random = dictNode[curr.random]
            curr = curr.next
        
        return dictNode[head]
        
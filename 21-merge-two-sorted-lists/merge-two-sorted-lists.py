# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummyNode = ListNode()
        temp = dummyNode
        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        if list1:
            temp.next = list1
        if list2:
            temp.next = list2
            
        return dummyNode.next

        # # create a temp node 
        # temp = ListNode()
        # currentNode = temp
        # # using 2 pointer 
        # point1 = list1
        # point2 = list2

        # # Use a while loop to compare va the values of the 2 pointers 
        # while point1 and point2:
        #     # Use a check condition to append the smaller value node to merged the list and move pointer 
        #     if point1.val < point2.val:
        #         currentNode.next = pointer1
        #         point1 = point1.next
        #     else:
        #         currentNode.next = pointer2
        #         point2 = point2.next

        # # After the loop, one of the list may have remaining nodes. I will attachted it to the remaining of the list 
        # if point1:
        #     currentNode.next = point1
        # # return the temp node 

        
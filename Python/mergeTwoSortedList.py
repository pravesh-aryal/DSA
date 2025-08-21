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
        newListHead = ListNode()
        newList = newListHead

        while (list1 and list2):
            if (list1.val < list2.val):
                newList.next = list1
                list1 = list1.next
            else:
                newList.next = list2
                list2 = list2.next
            newList = newList.next
        if list1:
            newList.next = list1
        if list2:
            newList.next = list2

        
        return newListHead.next

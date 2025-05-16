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
        dummy = hold = ListNode()

        # while both lists have values
        while list1 and list2:
            # list 1 is smaller
            if list1.val < list2.val:
                # add the value
                hold.next = list1
                # move the list along
                list1 = list1.next
            else:
                hold.next = list2
                list2 = list2.next
            # move to next space to place value
            hold = hold.next
        
        # fill in left overs
        hold.next = list1 or list2

        # return list from the start
        return dummy.next

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev, curr = None, head

        while curr:
            # store the next one in temp
            temp = curr.next
            # the current next is not the previous item
            curr.next = prev
            # current is now the prev
            prev = curr
            # the new current is the temp
            curr = temp
        
        return prev
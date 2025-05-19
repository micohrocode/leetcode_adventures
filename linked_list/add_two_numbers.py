# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        dummy = ListNode()
        res = dummy

        total = carry = 0

        # if there are more numbers or a carry over
        while l1 or l2 or carry:
            # total is equal to the carry over
            total = carry

            # add the numbers and move to the next numbers
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            
            # the number to add
            num = total % 10
            # the carry over
            carry = total // 10

            # set the node and move to the next
            dummy.next = ListNode(num)
            dummy = dummy.next

        return res.next
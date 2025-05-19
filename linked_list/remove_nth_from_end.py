# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        # get all the nodes
        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        # get the index to remove
        removeIndex = len(nodes) - n

        if removeIndex == 0:
            return head.next

        # remove the node and return the head
        nodes[removeIndex - 1].next = nodes[removeIndex].next
        return head
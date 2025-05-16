class Solution(object):
    def hasCycle(self, head):
        seen = set()

        # while there is a next to check
        while head:
            # check if it has been seen before
            if head in seen:
                return True
            # add it to the seen set
            seen.add(head)
            # move to the next one
            head = head.next
        
        return False
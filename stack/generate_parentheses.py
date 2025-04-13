class Solution(object):
    def generateParenthesis(self, n):
        stack = []
        res = []

        def backtrack(openN, closedN):
            # it is complete and valid, add to the result
            if openN == closedN == n:
                res.append("".join(stack))
                return
            
            if openN<n:
                # add open
                stack.append("(")
                # up the open count
                backtrack(openN + 1, closedN)
                # rest the stack, after the backtrack
                stack.pop()
            if closedN<openN:
                # add closed
                stack.append(")")
                # up the closed count
                backtrack(openN, closedN + 1)
                # rest the stack, after the backtrack
                stack.pop()

        backtrack(0, 0)
        return res
        
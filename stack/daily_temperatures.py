class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            # if there are items in the stack
            # and the current temp is greater
            while stack and t > stack[-1][0]:
                # remove the item
                stackT, stackInd = stack.pop()
                # set the result
                res[stackInd] = i - stackInd
            # add the temperature to the stack
            stack.append((t,i))
        
        return res
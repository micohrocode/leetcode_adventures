class Solution(object):
    def largestRectangleArea(self, heights):
        maxArea = 0
        stack = []

        for i, h in enumerate(heights):
            # get the start index for the height
            start = i
            # while there are items in the stack
            # and the most recent item is greater than
            # the current height
            while stack and stack[-1][1] > h:
                # pop the values from the end
                index, height = stack.pop()
                # check for a new max Area
                # of the popped height
                maxArea = max(maxArea, height * (i - index))
                # the new start is the index it can be extended to backwards
                start  = index
            stack.append((start,h))
        
        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea
        
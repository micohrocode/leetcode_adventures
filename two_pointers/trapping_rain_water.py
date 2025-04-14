class Solution(object):
    def trap(self, height):
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        leftMax = height[left]
        rightMax = height[right]
        res = 0

        while left < right:
            if leftMax < rightMax:
                # move to the next left spot
                left += 1
                # check for a new highest left spot
                leftMax = max(leftMax, height[left])
                # add a water block
                # for each difference between the max and current height
                res += leftMax - height[left]
            else:
                # move to the next right spot
                right -= 1
                # check for a new highest right spot
                rightMax = max(rightMax, height[right])
                # add a water block
                # for each difference between the max and current height
                res += rightMax - height[right]
        
        return res


        
class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        res = 0

        while left < right:
            # check the current area
            area = min(height[left],height[right]) * (right - left)
            res = max(res,area)

            if height[left] <= height[right]:
                # if left side is smaller look for a larger side
                left+=1
            else:
                # else look for a larger side from the right
                right-=1
        
        return res
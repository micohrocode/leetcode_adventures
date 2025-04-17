import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        # left and right pointers
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            # get the middle
            # k eating speed
            k = (left + right) // 2

            total_time = 0

            for p in piles:
                # get total time at that speed to eat it all
                total_time += math.ceil(float(p) / k)

            if total_time <= h:
                # if its in less than that time
                # it could be the result
                res = k
                # but check lower just in case
                right = k - 1
            else:
                # it was too slow, check higher
                left = k + 1
        
        return res
        
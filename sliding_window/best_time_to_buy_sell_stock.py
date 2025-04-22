class Solution(object):
    def maxProfit(self, prices):
        # set the pointers
        left = 0
        right = 1
        maxPrice = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                # check for the new profit
                profit = prices[right] - prices[left]
                # see if it is the new max
                maxPrice = max(maxPrice, profit)
            else:
                # the right is lower or equal
                # so move the left here
                left = right
            # always move the right over one
            right += 1
        
        return maxPrice
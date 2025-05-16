class Solution(object):
    def maxProfit(self, prices):
        final = 0

        start = prices[0]
        len1 = len(prices)

        for i in range(0,len1):
            if start < prices[i]:
                final += prices[i] - start
            start = prices[i]

        return final
        
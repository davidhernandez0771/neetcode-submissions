class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1 # buy and sell days
        maxP = 0 # Current max profit

        while r < len(prices): # while sell day hasnt gone through everyday
            if prices[l] < prices[r]: # if my buy day is less than the current sell day 
                profit = prices[r] - prices[l] # calculate profit
                maxP = max(maxP, profit) # compare to current, if bigger u keep it
            else: # the buy day is bigger than the sell day, no profit, switch l to r 
                l = r
            r += 1 # sell day always keeps moving no matter what
        return maxP
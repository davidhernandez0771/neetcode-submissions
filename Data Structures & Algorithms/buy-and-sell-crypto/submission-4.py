class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force

        maxP = 0
        for l in range(len(prices)):
            for r in range(l + 1, len(prices)):
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
        return maxP
                

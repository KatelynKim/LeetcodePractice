class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while r < len(prices):
            maxProfit = max(maxProfit, prices[r] - prices[l])
            if prices[r] <= prices[l]:
                l = r
                r = l + 1
            else:
                r += 1

        return maxProfit


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        l, r = 0, 1
        while l < r and r <= len(prices) - 1:
            if prices[l] >= prices[r]:
                l = r
                r = r + 1
            else:
                profit = prices[r] - prices[l]
                res = max(res, profit)
                r = r + 1
        return res
        
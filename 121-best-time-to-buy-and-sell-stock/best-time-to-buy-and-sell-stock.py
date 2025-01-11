class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # Using for loop
        indexBuy = 0
        maxProfit = 0 
        for i in range(len(prices)):
            if prices[i] > prices[indexBuy]:
                maxProfit = max(maxProfit, prices[i] - prices[indexBuy])
            else:
                indexBuy = i
        return maxProfit
            













        # # indexBuy = 0
        # # maxProfit = 0 
        # # for i in range(len(prices)):
        # #     if prices[i] < prices[indexBuy]:
        # #         indexBuy = i
        # #     maxProfit = max(maxProfit, prices[i] - prices[indexBuy])
        # # return maxProfit 

        # # Or using 2 pointer technique 
        # maxProfit = 0 
        # l, r = 0, 1
        # while r < len(prices):
        #     if prices[r] > prices[l]:
        #         maxProfit = max(maxProfit, prices[r] - prices[l])
        #     else:
        #         l = r  
        #     r += 1
        # return maxProfit

            
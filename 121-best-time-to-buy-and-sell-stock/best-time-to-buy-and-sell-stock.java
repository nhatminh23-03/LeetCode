class Solution {
    public int maxProfit(int[] prices) {
        int maxProfit = 0;
        int n = prices.length;
        int indexBuy = 0;
        for ( int i = 0; i < n; i++){
            if(prices[i] < prices[indexBuy]){
                indexBuy = i;
            }
            maxProfit = Math.max(maxProfit, prices[i] - prices[indexBuy]);
        }
        
        return maxProfit;
        
    }
}
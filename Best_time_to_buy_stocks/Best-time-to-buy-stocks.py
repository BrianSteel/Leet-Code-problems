from typing import List
import time


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = []
        min_price = prices[0]
        max_price = -1
        for p in prices:
            if min_price > p:
                profits.append(max_price - min_price)
                min_price = p
                max_price = -1
            elif max_price < p:
                max_price = p
        profits.append(max_price - min_price)
        return max(profits)

    def maxProfitII(self, prices: List[int]) -> int:#[7,1,5,3,6,4]
        length = len(prices)
        max_price = 0
        for p in range(length-1):
            if(prices[p+1] and prices[p] < prices[p+1]):
                max_price += prices[p+1] - prices[p]
        return max_price    

    def maxProfitIII(self, prices: List[int]) -> int:#[7,1,5,3,6,4]
        profits = []
        length = len(prices)
        for p in range(length-1):
            if(prices[p+1] and prices[p] < prices[p+1]):
                profits.append(prices[p+1] - prices[p])
        first_max = max(profits)
        profits.remove(first_max)
        second_max = max(profits)
        return first_max + second_max;

answ = Solution()
print(answ.maxProfitIII([3,3,5,0,0,3,1,4]))
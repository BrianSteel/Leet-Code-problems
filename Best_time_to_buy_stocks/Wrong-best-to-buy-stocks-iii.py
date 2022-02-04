from typing import List

class Solution:
    # account for consecutive increases
    # account for decrease
    # account for random increase or decrease 
    # CAN NOT account for consecutive increases along with random increases (prefers to skip to the consecutive increase)
    # eg - [1,2,4,2,5,7,2,4,9,0] ANS: 5-1 + 7-5 + 9-2
    def wrong_maxProfitIII(self, prices: List[int]) -> int:#[7,1,5,3,6,4]
        profits = []
        still_increasing = False
        length = len(prices)
        if(length == 0): return 0
        for p in range(length-1):
            if(prices[p+1] and prices[p] < prices[p+1]):
                if still_increasing and (not (p+1 == length-1) or len(profits) > 1):
                    profits_last_index = len(profits)-1
                    profits[profits_last_index] = profits[profits_last_index] + (prices[p+1] - prices[p]) # 1, 2, 3
                else:
                    profits.append(prices[p+1] - prices[p])

                # if prices[p+2] and prices[p+1] < prices[p+2]: why does not it work?? # prices[p+2] does not work in python
                if (length-1) >= (p+2) and prices[p+1] < prices[p+2]: # 1,3,5
                    still_increasing = True
                else: still_increasing = False


        profits_length = len(profits)

        if(profits_length == 0): return 0
        first_max = max(profits)
        if profits_length == 1: 
            return first_max
        else: 
            profits.remove(first_max)
            second_max = max(profits)
            return first_max + second_max
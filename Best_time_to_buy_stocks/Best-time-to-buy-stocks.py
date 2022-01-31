from cmath import inf
from tokenize import Number
from typing import List

from numpy import Inf


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # declare variables that will needed for caching data
        profits = []
        # The first value is always the min_price at first
        min_price = prices[0]
        # we dont know the max_price yet
        max_price = -1 # float('-inf')
        # just loop through the prices
        for p in prices:
            # we dont care about if the min_price is == to the current price
            # check if minimum price is greater than current value, then we know current value is the new minimum
            # so we assign current value as minimum and any max prices diff we found earlier is saved in case they turn out to be highest
            if min_price > p:
                # it could also that max diff is already found before the new min so it is saved before the min_price and max_price is changed
                profits.append(max_price - min_price)
                min_price = p
                # maximum price is set to default because currently this max is the max price before the new min price 
                # as we only care about the max after the min
                max_price = -1
            # this condition does the job of finding out the new maxs
            # min_price < p cant be used to check for max as everything will be greater than that minimum and correct max cant be found
            # eg for [7,1,5,3,6,4], the 1 will min and the last item 4 will be used for finding minimum which is wrong (ignore this if not needed)
            # It would accurate if we only check for values that is greater than the current max value
            elif max_price < p:
                max_price = p
        
        # use the final obtained max_price to find the diff
        profits.append(max_price - min_price)
        # return the maximum value among them
        return max(profits)

    def maxProfitII(self, prices: List[int]) -> int:#[7,1,5,3,6,4]
        # The idea is the if the next value is bigger than the previous just add to the difference
        # this is because eg 3, 5, 7. Here you buy at 3 and sell at 7 (diff = 4). Answer is same as 5-3 = 2, 7-5 =2 and 2+2 = 4
        # so add the diffs if number increase from the previous one and that's it as you can buy and unlimited times
        length = len(prices)
        max_price = 0
        # loops from 0 to length -1 (because if length is 4 the final value in the loop should be for index 3 as index 4 does not exist)
        for p in range(length-1):
            # check for last index because if length is 4, last index will be 3 and prices[3+1] which is prices[4] does not exist
            if(prices[p+1] and prices[p] < prices[p+1]):
                max_price += prices[p+1] - prices[p]
        return max_price    

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

    # def maxProfitIII():
    def maxProfitCooldown(self, prices:List[int]) -> int: # 1 2 4 0 2
        
        cache = {}
        def depthFirstSearch(i:int, decision:str):
            if len(prices) <= i: return 0
            if (i, decision) in cache:
                return cache[(i, decision)]
            
            cooldown = depthFirstSearch(i+1, 'b')
            if decision == 'b':
                profit = depthFirstSearch(i + 1, 's') - prices[i]
            else:
                profit = depthFirstSearch(i + 2, 'b') + prices[i]
            
            cache[(i, decision)] = max(profit, cooldown)
            return cache[(i, decision)]

        return depthFirstSearch(0, 'b')
            

ans = Solution()
print(ans.maxProfitCooldown([1,2,4,0,2]))

        



# def test_solution(cases: List[List[int]], solutions: List[int]):
#     solution_index = 0
#     for case in cases: 
#         answ = Solution()
#         print(answ.maxProfitIII(case), answ.maxProfitIII(case) == solutions[solution_index]) # [3,3,5,0,0,3,1,4]
#         solution_index += 1

# cases = [
#     [3,3,5,0,0,3,1,4],
#     [1,2,3], 
#     [1,2,3,4,5],
#     [2,5,8], 
#     [2,5,8,11,14],
#     [2, 10, 12], 
#     [2,10,12,14,15],
#     [2,10], 
#     [2,10,12,14,15,3,5,1],
#     [2,1], 
#     [10], 
#     [7,6,4,3,1], 
#     [],
#     [6,1,3,2,4,7], 
#     [1,2,4,2,5,7,2,4,9,0] 
# ] 
# solutions = [6, 2, 4, 6, 12, 10, 13, 8, 15, 0, 0, 0, 0, 7, 13]


# test_solution(cases, solutions)

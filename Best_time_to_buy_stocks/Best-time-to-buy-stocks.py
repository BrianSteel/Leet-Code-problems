from typing import List


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
                print(max_price, min_price, p)
                profits.append(max_price - min_price)
                min_price = p
                # maximum price is set to default because currently this max is the max price before the new min price 
                # as we only care about the max after the min
                max_price = -1
                print(max_price, min_price)
            # this condition does the job of finding out the new maxs
            # min_price < p cant be used to check for max as everything will be greater than that minimum and correct max cant be found
            # eg for [7,1,5,3,6,4], the 1 will min and the last item 4 will be used for finding minimum which is wrong (ignore this if not needed)
            # It would accurate if we only check for values that is greater than the current max value
            elif min_price < p:
                print(max_price, p)
                max_price = p
                print(max_price)
        
        # use the final obtained max_price to find the diff
        profits.append(max_price - min_price)
        print(profits)
        # return the maximum value among them
        return max(profits)

    def maxProfitII(self, prices: List[int]) -> int:#[7,1,5,3,6,4]
        # The idea is the if the next value is bigger than the previous just add to the difference
        # this is because eg 3, 5, 7. Here you buy at 3 and sell at 7 (diff = 4). Answer is same as 5-3 = 2, 7-5 =2 and 2+2 = 4
        # so add the diffs if number increase from the previous one and that's it as you can buy and unlimited times
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
print(answ.maxProfit([7,1,5,3,6,4])) # [3,3,5,0,0,3,1,4]
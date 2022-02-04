from cmath import inf
from tokenize import Number
from typing import List

from numpy import Inf


class Solution:
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
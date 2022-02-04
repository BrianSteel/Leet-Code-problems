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

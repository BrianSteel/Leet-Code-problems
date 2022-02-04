from typing import List

class Solution:
    # tree list formation 
    # dfs is carried out because we obtain and accumulate the results resulting from leaf nodes
    def maxProfitCooldown(self, prices:List[int]) -> int: # 1 2 4 0 2
        # memoisation through hashing, also can use 2d array with one axis for decision and one for i
        cache = {}
        def depthFirstSearch(i:int, decision:str):
            # if i is greater than length or equal to length of stock array just return 0
            # condition to return in case of no array or i gets too big due to increments due to recursion - CHOICE 1
            if len(prices) <= i: return 0
            # makes the code faster - CHOICE 2
            if (i, decision) in cache:
                return cache[(i, decision)]
            # the best result can be obtained from cooldown decision or buy decision or sell decision at any point
            # so here explore all nodes when cooldown decision is takes or all nodes under cooldown decision
            cooldown = depthFirstSearch(i+1, 'b')
            if decision == 'b':
                # if decision is buy, get profits for all nodes under any buying decision
                profit = depthFirstSearch(i + 1, 's') - prices[i]
            else:
                # get profit under selling decision
                profit = depthFirstSearch(i + 2, 'b') + prices[i]
            # at any node there is either selling or cooldown decision | buying or cooldown decision
            # take the max of cooldown or the other decision
            cache[(i, decision)] = max(profit, cooldown)
            # calculate the max profit decision for each leaf node and go up - CHOICE 3
            return cache[(i, decision)]

        # call and return the result of the recursive function
        return depthFirstSearch(0, 'b')
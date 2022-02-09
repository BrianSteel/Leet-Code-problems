from cmath import inf
from typing import List
from black import T
from tabulate import tabulate

class Solution:
    def maxProfit(self, prices: List[int], print_data=False) -> int:
        if(len(prices) == 0): return 0

        fb, sb = inf, inf
        fs, ss = 0, 0
        print_fb, print_fs, print_sb, print_ss = [], [], [], []

        # loop over the prices to check each price eg - 3,3,5,0,0,3,1,4
        for price in prices:
            old_fb = fb
            fb_prices = price
            # lowest 1st buying price is found at the right point (at index 4 for the eg)
            fb = min(fb, price) # 
            print_fb.append([price, old_fb, fb_prices, fb])

            old_fs = fs
            fs_prices = price-fb
            # 1st highest selling price is found at the right point (at index 5 for the eg)
            fs = max(fs, price-fb) 
            print_fs.append([price, old_fs, fs_prices, fs])

            old_sb = sb
            sb_prices = price-fs
            # second lowest buying price is found at the right point (at index 6 for the eg)
            sb = min(sb, price-fs) 
            print_sb.append([price, old_sb, sb_prices, sb])

            old_ss = ss
            ss_prices = price-sb
            # second highest selling price is found at the right point (at index 7 for the eg)
            ss = max(ss, price-sb) 
            print_ss.append([price, old_ss, ss_prices, ss])

        if(print_data):
            t = tabulate(print_fb, headers=['Prices', 'Old', 'Change', 'New'])
            print(t)
            t = tabulate(print_fs, headers=['Prices', 'Old', 'Change', 'New'])
            print(t)
            t = tabulate(print_sb, headers=['Prices', 'Old', 'Change', 'New'])
            print(t)
            t = tabulate(print_ss, headers=['Prices', 'Old', 'Change', 'New'])
            print(t)

        return ss
        
# ans = Solution()
# print(ans.maxProfit([3,3,5,0,0,3,1,4], True))


# def test_solution(cases: List[List[int]], solutions: List[int]):
#     solution_index = 0
#     for case in cases: 
#         answ = Solution()
#         print(answ.maxProfit(case), solutions[solution_index], answ.maxProfit(case) == solutions[solution_index]) # [3,3,5,0,0,3,1,4]
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
#     [1,2,4,2,5,7,2,4,9,0],
#     [1 , 500 , 5 , 1000]
# ] 
# solutions = [6, 2, 4, 6, 12, 10, 13, 8, 15, 0, 0, 0, 0, 7, 13, 1494]


# test_solution(cases, solutions)


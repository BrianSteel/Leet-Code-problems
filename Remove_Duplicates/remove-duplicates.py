from typing import List

from numpy import true_divide


class Solution:
    def removeDuplicate(self, list:List[int]):
        length = len(list)
        loop_length = length - 1

        # if length is zero or 1 there can be no duplicates
        if loop_length == 0 or length == 0: return False

        # sort the list so that we can make sure current item's next will always be greater or equal to it
        list = sorted(list)
        # loop over 0, 1, 2 ..... length - 1, if length 2 then 0, 1 and so on
        for index in range(loop_length):
            # if equal then duplicate is present
            if list[index] == list[index+1]:
                return True
        # else return false (no duplicates)
        return False
            

ans = Solution()
print(ans.removeDuplicate([3,3]))

# https://leetcode.com/problems/contains-duplicate-ii/
# https://leetcode.com/problems/contains-duplicate-iii/

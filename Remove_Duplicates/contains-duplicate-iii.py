from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        length = len(nums)
        cache = []
        # we are avoiding using object caching
        # store the number and its index in two dimensional array eg - [[2,1],[1,2]]
        for index in range(length):
            cache.append((nums[index], index))
        
        # 2D array cache is sorted
        cache = sorted(cache, key=lambda x: x[0])

        # loop till before the last element as i+1 is used
        # now it can check two numbers iteratively to see if the difference is less than or equal to t
        # if so they are nearby duplicates but now indexes need to be checked
        # if they are nearby duplicates and also index diff is <= k then true is returned
        for i in range(length-1):
            if abs(cache[i][0] - cache[i+1][0]) <= t and abs(cache[i][1] - cache[i+1][1]) <= k:
                return True

        return False

    # Need to find a O(N) solution

ans = Solution()
print(ans.containsNearbyAlmostDuplicate([3,3,1], 1, 1))
from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        length = len(nums)
        cache = []
        for index in range(length):
            cache.append((nums[index], index))
        
        cache = sorted(cache, key=lambda x: x[0])
        print(cache)

        for i in range(length-1):
            if abs(cache[i][0] - cache[i+1][0]) <= t and abs(cache[i][1] - cache[i+1][1]) <= k:
                return True

        return False

ans = Solution()
print(ans.containsNearbyAlmostDuplicate([3,3,1], 1, 1))
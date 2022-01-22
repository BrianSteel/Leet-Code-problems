from typing import List, Set

class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        set_array = set(nums)
        nums = list(set_array)
        return nums

ans = Solution()
print(ans.removeDuplicates([1,1,2]))
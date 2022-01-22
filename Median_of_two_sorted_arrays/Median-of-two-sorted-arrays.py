from math import floor
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        joined_list = nums1 + nums2
        sorted_list = sorted(joined_list)
        median_index = (len(sorted_list) + 1 ) / 2 - 1
        int_median_index = floor(median_index)
        list_length = len(sorted_list)
        median_value = 0
        if list_length % 2 == 0:
            median_value = (sorted_list[int_median_index] + sorted_list[int_median_index + 1]) / 2
        else:
            median_value = sorted_list[int_median_index]
        return median_value
        
answer = Solution()
print(answer.findMedianSortedArrays([1,2], [3,4]))
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # because the first no is unique
        i = 1
        length = len(nums)
        for j in range(length - 1):
            # compare the second number is greater than the first
            if nums[j + 1] > nums[j]:
                # then save the new greater number to the first repeat position 
                # in that way all the repeats will be replaced before length - 1 is reached
                nums[i] = nums[j+1]
                # increase the number upto which the non repeating numbers are
                i += 1
        # return that non repeating length of number
        return i
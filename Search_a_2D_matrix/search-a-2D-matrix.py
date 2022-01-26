import math
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # if length of matrix is 0, just return false
        if len(matrix) == 0: return False
        # to help save the row
        row_cache = []
        # loop through the rows of the matrix
        for row in matrix:
            # save to stop processing everytime
            row_start = row[0]
            row_end = row[len(row)-1]
            # check if target value could be within the start and end of each row
            if row_start <= target and row_end >= target: # [x] forgot equals
                if row_start == target or row_end == target: 
                    return True
                else:
                    # if target is there save that row, to loop through it later
                    row_cache = row
                    break
            # if target is less than start then there is no possibility that value is there
            # Because matrix has each value in ascending order
            if(target < row_start):
                return False

        # now loop through the items in that row to see target is present
        # for item in row_cache:
        #     if item == target:
        #         return True
        # binary search is better
        return self._binarySearch(0, len(row_cache)-1, target, row_cache)

    # implement binary search
    def _binarySearch(self, start_index, end_index, target, arr):
        # condition for termination of loop inside no target found
        if end_index >= start_index:
            mid_index = math.floor((start_index + end_index)/2)
            if arr[mid_index] == target:
                return True
            elif arr[mid_index] > target:
                # must use mid_index - 1 so that end_index can get less than start_index if target not present or loop does not terminate
                return self._binarySearch(start_index, mid_index-1, target, arr ) # [x] forgot return
            else:
                # must use mid_index+1 so that start_index can get more than end_index if target not present or loop does not terminate
                return self._binarySearch(mid_index+1, end_index, target, arr )
        else: return False

answer = Solution()
print(answer.searchMatrix([[1]], 1))
# check for [[1]], 1


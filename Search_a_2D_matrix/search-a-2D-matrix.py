from tkinter.tix import Tree
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # to help save the row
        row_cache = []
        # loop through the rows of the matrix
        for row in matrix:
            # save to stop processing everytime
            row_start = row[0]
            row_end = row[len(row)-1]
            # check if target value could be within the start and end of each row
            if row_start < target and row_end > target:
                if row_start == target or row_end == target: 
                    return True
                else:
                    # if target is there save that row, to loop through it later
                    row_cache = row
            # if target is less than start then there is no possibility that value is there
            # Because matrix has each value in ascending order
            if(target < row_start):
                return False

        # now loop through the items in that row to see target is present
        for item in row_cache:
            if item == target:
                return True

        return False

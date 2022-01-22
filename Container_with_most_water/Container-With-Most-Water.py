from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # set initial max area
        max_area = -1
        # set the first index pointer
        first_index = 0
        # set another pointer to last index
        end_index = len(height) - 1
        # create a loop to compare first and end index
        while first_index < end_index:
            # find shorter height of the first vs end index
            shorter_height = min(height[first_index], height[end_index])
            # calculate the width btn first and end index
            width = end_index - first_index
            # find the resulting area
            max_area = max(max_area, shorter_height * width)

            # update the condition
            if height[first_index] < height[end_index]: 
                first_index += 1
            else:
                end_index -= 1
        # return the max area
        return max_area

        
solution = Solution()
ans = solution.maxArea([3,3,3,16,16,6])
print(ans)

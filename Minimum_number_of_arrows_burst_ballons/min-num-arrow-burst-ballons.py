from typing import List

from matplotlib.pyplot import arrow

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0

        # sort based on the first diameter parameter to make the calculation easier 
        points = sorted(points, key=lambda x: x[0])
        
        # store the first item's second dia parameter
        ballon_dia = points[0][1]
        # if points has length min 1 arrow need to be shot and we can then start the loop from second item
        arrowToBeShot = 1

        # start the loop from second item
        for point in points[1:]:
            # in case the first parameter is less than or equal to stored second parameter
            # this means it is inside the diameter of the balloon and one arrow can take out boths/all
            # ----x
            #    y---- 
            # ex. explanation: we are checking if y is less or equal to x
            if ballon_dia >= point[0]: # [1,2], [3,4], [4,5]
                continue
            # if not increase the arrow shot and also change the current stored second parameter
            # because we have sorted the points and we dont need to take last 2nd dia parameter into account
            arrowToBeShot += 1
            ballon_dia = point[1]

        return arrowToBeShot

ans = Solution()
print(ans.findMinArrowShots([[1,4], [3,5], [4,6]]))

        
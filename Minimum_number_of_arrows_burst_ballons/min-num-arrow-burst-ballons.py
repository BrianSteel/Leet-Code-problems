from typing import List

from matplotlib.pyplot import arrow

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0

        # sort based on the first diameter parameter to make the calculation easier 
        # if first item has largest diameter, and then the others have all small diameters it wont give right result and return just 1
        # this is why we have sort based on the item's second value
        # [[1, 9], [1, 3], [2, 5], [2, 10], [3, 9], [7, 16], [7, 12], [9, 11], [9, 16]] check this to be sure
        points = sorted(points, key=lambda x: x[1]) 
        print(points)
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
print(ans.findMinArrowShots([[1,9],[7,16],[2,5],[7,12],[9,11],[2,10],[9,16],[3,9],[1,3]]))

        
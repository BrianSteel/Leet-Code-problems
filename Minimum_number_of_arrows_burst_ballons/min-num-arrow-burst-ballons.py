from typing import List

from matplotlib.pyplot import arrow

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0: return 0

        points = sorted(points, key=lambda x: x[0])
        
        ballon_dia = points[0][1]
        arrowToBeShot = 1

        for point in points[1:]:
            if ballon_dia >= point[0]: # [1,2], [3,4], [4,5]
                continue
            arrowToBeShot += 1
            ballon_dia = point[1]

        return arrowToBeShot

ans = Solution()
print(ans.findMinArrowShots([[1,4], [3,5], [4,6]]))

        
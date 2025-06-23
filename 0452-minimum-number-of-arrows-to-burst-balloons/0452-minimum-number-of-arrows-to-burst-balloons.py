class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:

        points.sort(key= lambda x: x[1])
        if not points:
            return 0
        arrowcount=1
        end = points[0][1]

        for start,finish in points[1:]:

            if start>end:
                arrowcount+=1
                end = finish
        return arrowcount 
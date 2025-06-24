class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals.sort(key= lambda x:x[0])
        if not intervals:
            return []
        end = intervals[0][1]
        prevstart = intervals[0][0]

        result =[]
        for  start,finish in intervals[1:]:
            if start<=end:
                end = max(end,finish)
            else:
                result.append([prevstart,end])
                prevstart= start
                end = finish

        result.append([prevstart,end])
        return result


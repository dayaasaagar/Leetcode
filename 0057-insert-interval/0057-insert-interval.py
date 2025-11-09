class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        results =[]
        i=0
        ns,ne = newInterval
        n = len(intervals)

        while i< n and intervals[i][1] < ns:
            results.append(intervals[i])
            i+=1
        
        while i<n and intervals[i][0] <= ne:
            ns = min(intervals[i][0],ns)
            ne = max(intervals[i][1],ne)
            i+=1
        results.append([ns,ne])
        
        while i<n:
            results.append(intervals[i])
            i+=1
        return results 

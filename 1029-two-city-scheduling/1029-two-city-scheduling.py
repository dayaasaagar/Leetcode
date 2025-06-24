class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key= lambda x:x[0]-x[1])
        totala =0
        totalb=0
        n=len(costs)//2

        for i in range(n):
            totala+=costs[i][0]
        for i in range(n,len(costs)):
            totalb+=costs[i][1]
        
        return totala+totalb


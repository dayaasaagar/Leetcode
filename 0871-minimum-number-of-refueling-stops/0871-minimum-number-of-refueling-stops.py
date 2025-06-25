class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:

        prevpos =0
        max_heap=[]
        fuel =startFuel
        refuels =0
        stations.append([target,0])

        for pos,gas in stations:

            fuel -=pos - prevpos

            while fuel<0 and max_heap:
                fuel+=-heapq.heappop(max_heap)
                refuels+=1
            
            if fuel<0:
                return -1
            
            heapq.heappush(max_heap,-gas)
            prevpos=pos
        return refuels
        


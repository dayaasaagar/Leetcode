class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = {i:[] for i in range(1,n+1)}
        for u,v,w in times:
            graph[u].append((v,w))

        min_heap=[(0,k)]
        dist ={}

        while min_heap:
            time,node = heapq.heappop(min_heap)
            if node in dist:
                continue
            dist[node]=time
            for nei,wt in graph[node]:
                heapq.heappush(min_heap,(wt+time,nei))
        
        return max(dist.values()) if len(dist)==n else -1 



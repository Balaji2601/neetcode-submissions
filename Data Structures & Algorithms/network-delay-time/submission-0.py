from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj = defaultdict(list)

        for u, v, wt in times:
            adj[u].append((v,wt))
        
        result = [float("inf")]*(n+1)

        result[k] = 0
        pq = []
        heapq.heappush(pq, (0, k))

        while pq:
            dist,u = heapq.heappop(pq)

            if dist > result[u]:
                continue
            
            for v, wt in adj[u]:
                if dist+wt < result[v]:
                    result[v] = dist+wt
                    heapq.heappush(pq, (result[v], v))
        
        for i in range(1, n+1):
            if result[i] == float("inf"):
                return -1
        
        return max(result[1:])
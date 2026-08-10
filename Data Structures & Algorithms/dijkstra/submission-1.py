import heapq
from collections import defaultdict

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        adj = defaultdict(list)
        for u,v,wt in edges:
            adj[u].append((v,wt))

        result = [float("inf")]*n
        result[src] = 0
        pq = [(0,src)]

        while pq:
            d, u = heapq.heappop(pq)
            if d > result[u]:
                continue
            
            for v, wt in adj[u]:
                if d+wt < result[v]:
                    result[v] = d+wt
                    heapq.heappush(pq, (d+wt, v))
        
        ans = {}
        for i in range(n):
            if result[i] == float("inf"):
                ans[i] = -1
            else:
                ans[i] = result[i]
        
        return ans

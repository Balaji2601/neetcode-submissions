from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def DFS(adj, u, visited):
            visited[u] = True

            for v in adj[u]:
                if not visited[v]:
                    DFS(adj, v, visited)

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = [False]*n
        ans = 0

        for i in range(n):
            if not visited[i]:
                DFS(adj, i, visited)
                ans += 1
        
        return ans

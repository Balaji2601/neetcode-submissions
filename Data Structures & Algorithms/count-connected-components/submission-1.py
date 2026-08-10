from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        def dfs(adj, u, visited):
            visited[u] = True

            for v in adj[u]:
                if not visited[v]:
                    dfs(adj, v, visited)


        adj = defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        count = 0
        visited = [False]*n
        for i in range(n):
            if not visited[i]:
                dfs(adj, i, visited)
                count += 1 
        
        return count
        
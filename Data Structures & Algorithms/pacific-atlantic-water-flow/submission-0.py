class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        pacific_visited = [[False]*n for _ in range(m)]
        atlantic_visited = [[False]*n for _ in range(m)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def bound(i, j, visited, prev):
            if 0 <= i < m and 0 <= j < n and not visited[i][j] and prev <= heights[i][j]:
                return True
            return False

        def dfs(i, j, visited):
            visited[i][j] = True
            
            for di, dj in directions:
                ni, nj = i+di, j+dj
                if bound(ni, nj, visited, heights[i][j]):
                    dfs(ni, nj, visited)


        for i in range(m):
            dfs(i, 0, pacific_visited)
            dfs(i, n-1, atlantic_visited)
        
        for j in range(n):
            dfs(0,j, pacific_visited)
            dfs(m-1, j, atlantic_visited)
        
        ans = []
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    ans.append([i,j])
        return ans
                    
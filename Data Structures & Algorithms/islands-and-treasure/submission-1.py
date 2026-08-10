class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque([])
        m = len(grid)
        n = len(grid[0])

        def bound(i, j):
            if 0 <= i < m and 0 <= j < n and result[i][j] != -1 and result[i][j] != 0 and result[i][j] == -2:
                return True
            return False
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        result = [[-2]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j, 0))
                    result[i][j] = 0
                elif grid[i][j] == -1:
                    result[i][j] = -1
        
        while q:
            i, j, dist = q.popleft()

            for di, dj in directions:
                ni = i+di
                nj = j+dj

                if bound(ni, nj):
                    result[ni][nj] = 1 + result[i][j]
                    q.append((ni,nj,result[ni][nj]))
        
        for i in range(m):
            for j in range(n):
                if result[i][j] == -2:
                    continue
                grid[i][j] = result[i][j]
        


        
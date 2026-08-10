class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        result = [[float("inf")]*cols for _ in range(rows)]

        def bound(i, j):
            if 0 <= i < rows and 0 <= j < cols:
                return True
            return False
        pq = [(0,0,0)] # effort, x, y
        result[0][0] = 0

        while pq:
            dist, i, j = heapq.heappop(pq)

            if dist > result[i][j]:
                continue
            
            for di, dj in directions:
                ni = i+di
                nj = j+dj

                if bound(ni, nj):
                    curr_effort = abs(heights[i][j] - heights[ni][nj])
                    new_effort = max(curr_effort, dist)
                    if new_effort < result[ni][nj]:
                        result[ni][nj] = new_effort
                        heapq.heappush(pq, (new_effort, ni, nj))
            
        return result[rows-1][cols-1]



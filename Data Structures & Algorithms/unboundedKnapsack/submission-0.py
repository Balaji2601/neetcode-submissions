class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        d = {}
        def solve(i,W):
            if W == 0:
                return 0
            if i == n:
                return 0
            if (i,W) in d:
                return d[(i,W)]
            
            pick = 0
            if weight[i] <= W:
                pick = profit[i] + solve(i,W-weight[i])
            
            skip = solve(i+1,W)

            d[(i,W)] = max(pick,skip)

            return d[(i,W)]
        
        return solve(0,capacity)
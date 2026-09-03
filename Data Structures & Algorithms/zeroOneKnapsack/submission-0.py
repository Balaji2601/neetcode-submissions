class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        n = len(profit)
        dp = {}
        def solve(i,W):
            if W == 0:
                return 0
            if i == n:
                return 0
            if (i,W) in dp:
                return dp[(i,W)]
            # pick
            pick = 0
            if weight[i] <= W:
                pick = profit[i] + solve(i+1,W-weight[i])
            
            skip = solve(i+1,W)
            dp[(i,W)] = max(skip,pick)
            return dp[(i,W)]
        
        return solve(0,capacity)


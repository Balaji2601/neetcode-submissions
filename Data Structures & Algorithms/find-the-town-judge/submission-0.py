class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        in_order = [0]*(n+1)
        out_order = [0]*(n+1)
        for u, v in trust:
            in_order[v] += 1
            out_order[u] += 1
        
        for i in range(1,n+1):
            if in_order[i] == n-1 and out_order[i] == 0:
                return i
        return -1
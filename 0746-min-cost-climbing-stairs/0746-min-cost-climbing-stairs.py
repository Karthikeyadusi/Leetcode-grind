class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = [None] * (n+1)
        for i in range(n,-1,-1):
            if i>= n:
                minCost[i] = 0
            elif i == (n-1):
                minCost[i] = cost[i]
            else:
                minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])
        return min(minCost[0], minCost[1])

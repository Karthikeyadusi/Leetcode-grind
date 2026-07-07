class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        minCost = [None] * (n+2)
        minCost[n]= 0
        minCost[n+1] = 0
        for i in range(n-1,-1,-1):
            minCost[i] = cost[i] + min(minCost[i+1], minCost[i+2])
        return min(minCost[0], minCost[1])

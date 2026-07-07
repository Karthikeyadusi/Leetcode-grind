class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        answers = [None] * (len(cost))
        def minCost(n):
            if n >=len(cost):
                return 0
            if answers[n] is not None:
                return answers[n]
            else:
                answers[n] = cost[n] + min(minCost(n+1), minCost(n+2))
                return answers[n]            
        return min(minCost(0) , minCost(1))
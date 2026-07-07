class Solution:
    def climbStairs(self, n: int) -> int:
        answers = [None] * (n+1)
        answers[0], answers[1] = 1,1
        def solve(n):
            if answers[n] is not None:
                return answers[n]
            else:
                answers[n] = solve(n-1) + solve(n-2)
                return answers[n]
        return solve(n)
        
        
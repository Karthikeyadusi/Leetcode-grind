class Solution:
    def fib(self, n: int) -> int:
        prev1 , prev2 = 0,1
        if n == 0:
            return prev1
        for i in range(n-1):
            current = prev1 + prev2
            prev1 = prev2
            prev2 = current
        return prev2

        
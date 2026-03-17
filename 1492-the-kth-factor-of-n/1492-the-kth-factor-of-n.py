class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        Factors = []
        for i in range(1,n+1):
            if n % i == 0:
                Factors.append(i)
        if k > len(Factors):
            return -1
        else:
            return Factors[k-1]
        
class Solution:
    def tribonacci(self, n: int) -> int:
        f = [0,1,1]
        if n<3:
            return f[n]
        for i in range(3,n+1):
            val = f[i-3] + f[i-2]  + f[i-1]
            f.append(val)
        return f[n]
        
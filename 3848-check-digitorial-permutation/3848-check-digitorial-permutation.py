import math
class Solution:
    def isDigitorialPermutation(self, n: int) -> bool:
        total = 0
        temp = n
        while n>0:
            digit = n % 10
            total += math.factorial(digit)
            n = n//10
        org = list(str(temp))
        res = list(str(total))
        print(org,res)
        return sorted(org) == sorted(res)
        
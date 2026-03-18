from math import isqrt
class Solution:
    def primePalindrome(self, n: int) -> int:
        def checkPrime(num: int):
            if num == 1:
                return False
            for i in range(2,(isqrt(num)+1)):
                if num % i == 0:
                    return False
            return True
        
        def checkPalindrome(num: int):
            rev_num = int(str(num)[::-1])
            if rev_num == num:
                return True
            else:
                return False
        i = n
        while i >=n:
            if checkPalindrome(i):
                if checkPrime(i):
                   return i
            i+=1
            if i <= 11:
                continue
            else:
                if len(str(i))%2 == 0 and i !=11:
                   i = 10 ** len(str(i))
        
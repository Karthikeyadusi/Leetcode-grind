class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def dp(n):
            temp = n
            product = 1
            while temp!=0:
                digit = temp%10
                product *= digit
                temp= temp//10
            return product
        while dp(n) % t != 0:
            n+=1
        return n

        
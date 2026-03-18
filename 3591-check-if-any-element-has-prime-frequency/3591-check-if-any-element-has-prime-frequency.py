class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        def checkPrime(n: int):
            if n == 1:
                return False
            for i in range(2,n):
                if n % i == 0:
                    return False
            return True
        for word in nums:
            if checkPrime(nums.count(word)):
                return True
        return False
        
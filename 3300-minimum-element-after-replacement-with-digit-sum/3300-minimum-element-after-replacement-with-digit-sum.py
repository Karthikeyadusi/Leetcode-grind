class Solution:
    def minElement(self, nums: List[int]) -> int:
        result= []
        def sumofdigits(n):
            temp = n
            total=0
            while temp != 0:
                digit = temp%10
                total+=digit
                temp= temp//10
            return total
        for num in nums:
            value = sumofdigits(num)
            result.append(value)
        return min(result)

        
        
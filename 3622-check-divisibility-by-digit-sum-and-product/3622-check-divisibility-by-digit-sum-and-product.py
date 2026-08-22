class Solution:
    def checkDivisibility(self, n: int) -> bool:
        digits_sum = 0
        digits_product = 1
        temp = n
        while temp != 0:
            digit = temp % 10
            digits_sum += digit
            digits_product *= digit
            temp = temp//10
        total = digits_sum + digits_product
        return n % total == 0

        
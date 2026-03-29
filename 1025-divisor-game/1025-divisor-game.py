class Solution:
    def divisorGame(self, n: int) -> bool:
        if n == 1:
            return False
        elif n % 2 == 0:
            return True
        else:
            return False
                
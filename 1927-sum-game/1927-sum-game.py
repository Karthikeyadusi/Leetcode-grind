class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        mid = n // 2

        left_sum = 0
        right_sum = 0
        leftq = 0
        rightq = 0


        for i in range(mid):
            if num[i] == "?":
                leftq+=1
            else:
                left_sum += int(num[i])
        
        for i in range(mid, n):
            if num[i] == "?":
                rightq+=1
            else:
                right_sum += int(num[i])
        totalq = leftq + rightq

        if totalq % 2 != 0:
            return True

        diff = left_sum - right_sum
        qdiff = leftq - rightq
        
        
        return diff != -9 * qdiff // 2
        

        
class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(2,len(arr)):
            if arr[i] % 2 != 0:
                if arr[i-1] % 2 !=0:
                    if arr[i-2] %2 !=0:
                        return True
        return False
        
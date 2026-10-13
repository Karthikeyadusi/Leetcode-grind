class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i, num in enumerate(nums):
            if num < 0:
                nums[i] = abs(nums[i])
        sorts = sorted(nums)[::-1]
        print(sorts)
        left = 0
        right = len(nums) - 1
        total = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                total += sorts[left] ** 2
                left+=1
            else:
                total-= sorts[right] **2
                right-=1
        return total
        

                
        
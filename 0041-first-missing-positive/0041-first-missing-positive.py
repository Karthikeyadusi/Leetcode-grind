class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        next_positive = 1
        nums[:] = sorted(nums)
        for i in range(0,len(nums)):
            if next_positive == nums[i]:
                next_positive+=1
        return next_positive



                


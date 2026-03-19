class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        low = 0
        high  = len(nums) -1

        for i in range(0,len(nums)-1):
            if nums[i] + 1 <= nums[i+1]:
                continue
            else:
                return i
            
        
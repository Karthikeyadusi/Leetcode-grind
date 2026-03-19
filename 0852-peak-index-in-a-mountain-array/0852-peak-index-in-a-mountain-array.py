class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        return nums.index(max(nums))
        
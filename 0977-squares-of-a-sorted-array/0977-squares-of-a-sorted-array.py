class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            temp = nums[i] ** 2
            nums[i] = temp
        return sorted(nums)
        
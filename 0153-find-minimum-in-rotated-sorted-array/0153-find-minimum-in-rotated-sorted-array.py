class Solution:
    def findMin(self, nums: List[int]) -> int:
        for i  in range(0,len(nums)):
            if i == 0:
                minimum = nums[i]
            if minimum > nums[i]:
                minimum = nums[i]
        return minimum
        
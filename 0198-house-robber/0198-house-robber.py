class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        next1 = 0
        next2 = 0
        for i in range(len(nums)-1,-1,-1):
            current = max((next2 + nums[i]), next1)
            next2 = next1
            next1 = current
        return next1

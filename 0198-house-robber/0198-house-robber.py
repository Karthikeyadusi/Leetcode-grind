class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxMoney = [0] * (n+2)
        for i in range(n-1,-1,-1):
            maxMoney[i] = max((nums[i] + maxMoney[i+2]), maxMoney[i+1])
        return maxMoney[0]
        
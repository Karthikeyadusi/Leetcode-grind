class Solution:
    def rob(self, nums: List[int]) -> int:
        answers = [None] * ((len(nums)+1))
        def maxMoney(n):
            if n >= len(nums) :
                return 0
            if answers[n] is not None:
                return answers[n]
            answers[n] = max((nums[n] + maxMoney(n+2)), maxMoney(n+1))
            return answers[n]
        return maxMoney(0)
            
        
        
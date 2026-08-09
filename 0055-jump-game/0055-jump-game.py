class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(0,len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, (i+nums[i]))
        return True
            

        
class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        if set(nums) == {0}:
            return 0
        for num in nums:
            total_xor ^= num
        if total_xor > 0:
            return len(nums)
        else:
            return len(nums) - 1




        
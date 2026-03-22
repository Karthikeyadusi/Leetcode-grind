class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        non_repeat = 0
        for num in nums:
            non_repeat ^= num
        return non_repeat

        
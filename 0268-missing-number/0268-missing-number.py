class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        expected = len(nums) *((len(nums))+1)//2
        given = sum(nums)

        return expected - given


            
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        one = 0
        two = 1
        if len(nums) == 1:
            return nums[0]
        while two < len(nums):
            if nums[one] == nums[two]:
                one+=2
                two+=2
            else:
                return nums[one]
        return nums[one]
                
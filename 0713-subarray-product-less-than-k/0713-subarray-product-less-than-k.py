class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        count = 0
        product = 1
        for right in range(0,len(nums)):
            adding = nums[right]
            product *= adding
            while product >=k:
                product = product//nums[left]
                left+=1
            count+=(right-left+1)
        return count

        
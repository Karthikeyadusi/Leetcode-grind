class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = nums[:]
        for num in nums:
            if num == val:
                result.remove(num)
        nums[:] = result[:]
        return len(result)
        
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        close = 0

        for i in range(0, len(nums)):
            if nums[i] == target : 
                return i
            elif nums[i] > target:
                return i
        return len(nums)
        """low = 0
        high = len(nums)-1

        while low < high:
            mid = (low+high)//2
            if target < nums[mid]:
                low+=1
                high = nums[mid]
            elif target > nums[mid]:
                low = nums[mid]
                high-=1
            elif target == nums[mid]:
                return mid
        if target!=mid:
            return low-1
"""
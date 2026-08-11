class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        chunk1 = nums[0:len(nums)-k]
        chunk2 = nums[len(nums)-k:]
        nums[:] = chunk2 + chunk1


        
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        arr = sorted(nums)

        for i in range(0,len(arr)):
            if arr[i] == arr[i+1]:
                return arr[i]

        
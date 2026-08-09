class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        h = {}
        for num in nums:
            h[num] = h.get(num,0) + 1
        for key in h:
            if h[key] > 1:
                return key

        # arr = sorted(nums)

        # for i in range(0,len(arr)):
        #     if arr[i] == arr[i+1]:
        #         return arr[i]

        
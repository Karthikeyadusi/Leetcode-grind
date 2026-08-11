class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        for i in range(1,len(nums) + 1):
            if i not in h:
                missing = i
            elif h[i] > 1:
                duplicate = i
        return [duplicate, missing]
        
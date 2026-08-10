class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        target = len(nums)/2
        for num in nums:
            h[num] = h.get(num, 0) + 1
        for key in h:
            if h[key] > target:
                return key
        
        
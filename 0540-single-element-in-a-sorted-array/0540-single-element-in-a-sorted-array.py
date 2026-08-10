class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        for key in h:
            if h[key] == 1:
                return key

                
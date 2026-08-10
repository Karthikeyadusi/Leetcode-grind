class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = []
        h = {}
        for num in nums:
            h[num] = h.get(num, 0) + 1
        for key in h:
            if h[key] == 1:
                res.append(key)
            if len(res) == 2:
                return res

        
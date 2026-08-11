class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        sort = sorted(nums)
        arr = []
        res = []
        for i in range(sort[0],sort[-1]+1):
            arr.append(i)
        for num in arr:
            if num not in sort:
                res.append(num)
        return res


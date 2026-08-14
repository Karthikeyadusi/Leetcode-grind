class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        nums = sorted(arr)[::-1]
        largest = len(set(nums))
        print(largest)
        res = []
        h = {}
        for num in nums:
            if num not in h:
               h[num] = largest
               largest-=1
        for key in arr:
            res.append(h[key])
        return res
        

        
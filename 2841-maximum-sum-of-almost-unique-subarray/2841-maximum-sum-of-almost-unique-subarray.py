class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        h = {}
        for num in nums[0:k]:
            h[num] = h.get(num, 0) + 1
        total = sum(nums[0:k])
        max_total = 0
        if len(h) >= m:
            max_total = total
        for i in range(1,len(nums)-k+1):
            removing = nums[i-1]
            adding = nums[i+k-1]
            total = total - removing + adding
            h[removing]-=1
            if h[removing] == 0:
                del h[removing]
            h[adding] = h.get(adding, 0) + 1
            if len(h) >= m:
                if total > max_total:
                    max_total = total
        return max_total        
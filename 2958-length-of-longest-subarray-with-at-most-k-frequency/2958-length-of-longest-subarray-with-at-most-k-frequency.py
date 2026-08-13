class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        h = {}
        left = 0
        best = 0
        for right in range(0,len(nums)):
            adding = nums[right]
            h[adding] = h.get(adding, 0) + 1
            while h[adding] > k:
                h[nums[left]]-=1
                if h[nums[left]] == 0:
                    del h[nums[left]]
                left+=1
            best = max(best, right-left+1)
        return best


        
        
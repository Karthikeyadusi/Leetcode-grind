class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        h = {}
        window = nums[0:k]
        for w in window:
            h[w] = h.get(w, 0) + 1
        total = sum(window)
        max_total = 0
        if len(h) == k:
            max_total = total
        for i in range(1,len(nums)-k+1):
            removing = nums[i-1]
            adding = nums[i+k-1]
            total = total - removing + adding
            h[removing] -=1
            if h[removing] == 0:
                del h[removing]
            h[adding] = h.get(adding, 0) + 1
            if len(h) == k:
                if total > max_total:
                    max_total = total
        return max_total



























        #brute force appraoch ig

        # def checkdiff(window,k):
        #     h = {}
        #     for w in window:
        #         h[w] = h.get(w,0) + 1
        #     if len(h) == k:
        #         return True
        #     return False
        # window = nums[0:k]
        # if checkdiff(window,k):
        #     total = sum(window)
        # else:
        #     total = 0
        # max_total = total
        # for i in range(1,len(nums)-k+1):
        #     window = nums[i:i+k]
        #     if checkdiff(window,k):
        #         total = sum(window)
        #     else:
        #         total = 0
        #     if total > max_total:
        #         max_total = total
        # return max_total

        

        
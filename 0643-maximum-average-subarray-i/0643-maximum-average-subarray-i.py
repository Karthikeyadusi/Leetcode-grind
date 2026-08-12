class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = sum(nums[0:k])
        max_total = total
        for i in range(1,len(nums)-k+1):
            total = total - nums[i-1] + nums[i+k-1]
            if total > max_total:
                max_total = total
        return (max_total/k)
        
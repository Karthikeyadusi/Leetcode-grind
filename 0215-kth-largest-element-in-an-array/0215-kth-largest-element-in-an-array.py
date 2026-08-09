import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        x = 0
        heap = []
        for num in nums:
            heapq.heappush(heap,-num)
        print(heap)
        for i in range(0,k):
            x = heapq.heappop(heap)
        return -x

        
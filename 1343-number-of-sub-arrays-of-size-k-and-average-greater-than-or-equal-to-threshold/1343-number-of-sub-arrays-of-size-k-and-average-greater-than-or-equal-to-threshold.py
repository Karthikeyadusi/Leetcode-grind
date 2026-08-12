class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        total = sum(arr[0:k])
        avg = total/k
        if avg>=threshold:
            count = 1
        else:
            count = 0
        for i in range(1,len(arr)-k+1):
            total = total - arr[i-1] + arr[i+k-1]
            avg = total/k
            if avg >= threshold:
                count+=1
        return count        
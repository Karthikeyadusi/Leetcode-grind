class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = nums1 + nums2
        result = sorted(combined)
        print(result)
        length  = len(result)
        if length < 2:
            return result[0]
        if length %2 != 0 :
            return float(result[length//2])
        else:
            return float(((result[length//2]+(result[(length//2)-1])))/2)
        
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = set()
        len1 = len(nums1)
        len2 = len(nums2)
        for i in range(0,len(nums1)):
            if nums1[i] in nums2:
                res.add(nums1[i])
        return list(res)

        
        
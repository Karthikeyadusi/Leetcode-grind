class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ans = list(set(nums))
        return not(len(ans) == len(nums))
        
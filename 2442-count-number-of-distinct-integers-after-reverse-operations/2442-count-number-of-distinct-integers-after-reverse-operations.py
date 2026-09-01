class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        def reverse(n):
            rev = int(str(n)[::-1])
            return rev
        new = nums.copy()
        for num in nums:
            r = reverse(num)
            new.append(r)
        return len(set(new))
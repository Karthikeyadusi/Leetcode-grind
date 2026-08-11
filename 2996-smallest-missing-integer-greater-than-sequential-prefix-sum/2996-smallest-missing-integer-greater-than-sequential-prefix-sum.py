class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        ans = 0
        prefix = []
        for i in range(0,len(nums)):
            if i == len(nums) - 1:
                prefix.append(nums[i])
            elif nums[i] + 1 == nums[i+1]:
                prefix.append(nums[i])
            else:
                prefix.append(nums[i])
                break
        total = sum(prefix)
        while total in nums:
            total+=1
        return total

        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        total = 0
        for i in range(0,len(nums)):
            total = nums[i]
            for j in range(i+1, len(nums)):
                if total + nums[j] == target:
                    return [i,j]
        

                
            
        
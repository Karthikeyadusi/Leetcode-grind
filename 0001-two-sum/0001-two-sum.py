class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i in range(0,len(nums)):

            com = target - nums[i]

            if com in h:
                return [i,h[com][0]]
            
            h[nums[i]] = i,nums[i]












        # total = 0
        # for i in range(0,len(nums)):
        #     total = nums[i]
        #     for j in range(i+1, len(nums)):
        #         if total + nums[j] == target:
        #             return [i,j]
        

                
            
        
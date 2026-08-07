class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # counts = {}
        # for i in nums:
        #     value = counts.get(i,0)
        #     if value>1:
        #         return True
        #     else:
        #         counts[i] = counts.get(i,0) + 1
        #         if counts.get(i,0) > 1:
        #             return True
        # return False
        
        # set_nums = set()
        # for num in nums:
        #     if num in set_nums:
        #         return True
        #     set_nums.add(num)
        # return False

        res = list(set(nums))
        return not(len(nums) == len(res))

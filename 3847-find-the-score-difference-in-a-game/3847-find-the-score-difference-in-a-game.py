class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        person1 = True
        person2 = False  
        p1 = 0
        p2 = 0
        for i in range(0,len(nums)):
            if nums[i] % 2 != 0 :
                person1, person2 = person2, person1
            if (i+1) % 6 == 0:
                    person1, person2 = person2, person1
            if person1:
                p1 += nums[i]
            else:
                p2 += nums[i]
        return p1 - p2


            


        
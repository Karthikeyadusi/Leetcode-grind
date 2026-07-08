class Solution:
    def jump(self, nums: List[int]) -> int:
        memory = [None] * (len(nums) + 1)
        def minJumps(n):
            answer = []
            if n>= len(nums)-1:
                return 0
            if memory[n] is not None:
                return memory[n]
            if nums[n] == 0:
                memory[n] = float("inf")
                answer.append(memory[n])
            for i in range(1, nums[n]+1):
                answer.append(1 + minJumps(i+n))
            memory[n] = min(answer)
            return memory[n]
        return minJumps(0)
            
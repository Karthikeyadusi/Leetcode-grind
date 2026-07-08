class Solution:
    def jump(self, nums: List[int]) -> int:
        memory = [None] * (len(nums) + 1)
        last = len(nums) - 1
        memory[last] = 0
        for i in range(last-1, -1, -1):
            answer = []
            if nums[i] == 0:
                answer.append(float("inf"))
            for j in range(1, nums[i]+1):
                next = i + j
                if next >= last:
                    answer.append(1)
                else:
                    answer.append(1+memory[next])
            memory[i] = min(answer)
        return memory[0]
            
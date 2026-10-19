class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        arr = sorted(nums)
        result = []
        for i, num in enumerate(arr):
            if num == target:
                result.append(i)
        return result

        
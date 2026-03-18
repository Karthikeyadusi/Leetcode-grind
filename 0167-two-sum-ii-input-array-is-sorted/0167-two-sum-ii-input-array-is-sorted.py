class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) -1
        result = []
        while left<right:
            current_sum = numbers[left] + numbers[right]
            if current_sum == target:
                result.append(left+1)
                result.append(right+1)
                break
            elif current_sum < target:
                left+=1
            elif current_sum>target:
                right-=1
        return result

            

        
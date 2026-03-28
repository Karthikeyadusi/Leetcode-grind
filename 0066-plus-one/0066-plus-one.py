class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
            string = ""
            result = []
            for digit in digits:
                string += str(digit)
            num = int(string)
            next_num = num + 1
            new_str = str(next_num)
            for s in new_str:
                result.append(int(s))
            return result


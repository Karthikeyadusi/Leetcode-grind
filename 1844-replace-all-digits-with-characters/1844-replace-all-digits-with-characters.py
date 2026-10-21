class Solution:
    def replaceDigits(self, s: str) -> str:
        nums = "0123456789"
        result = ""
        for i, letter in enumerate(s):
            if letter not in nums:
                result+=letter
            elif letter in nums:
                temp1 = ord(s[i-1])
                temp1+=int(letter)
                ch = chr(temp1)
                result+=ch
        return result
        
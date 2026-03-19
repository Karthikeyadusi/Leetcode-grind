class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""
        for char in s:
            if char.isalnum():
                cleaned += "".join(char.lower())
        print(cleaned)

        low = 0
        high = len(cleaned) - 1
        while low < high:
            if cleaned[low] != cleaned[high]:
                return False
            else:
                low+=1
                high-=1
        return True

        
class Solution:
    def reverseDegree(self, s: str) -> int:
        i = 26
        h = {}
        totals = []
        string = "abcdefghijklmnopqrstuvwxyz"
        for letter in string:
            h[letter] = i
            i-=1
        for j in range(0,len(s)):
            value = h[s[j]] * (j+1)
            totals.append(value)
        return sum(totals)
            
        
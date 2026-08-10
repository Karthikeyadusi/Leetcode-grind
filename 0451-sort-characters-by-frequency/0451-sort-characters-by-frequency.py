class Solution:
    def frequencySort(self, s: str) -> str:
        h = {}
        res = ""
        for letter in s:
            h[letter] = h.get(letter, 0) + 1
        for count in range(len(s),0,-1):
            for key in h:
                if h[key] == count:
                    res += key * count
        return res
        
        

        

        
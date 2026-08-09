class Solution:
    def firstUniqChar(self, s: str) -> int:
        h = {}
        for letter in s:
            h[letter] = h.get(letter,0) + 1
        for key in h:
            if h[key] == 1:
                return s.index(key)
        return -1
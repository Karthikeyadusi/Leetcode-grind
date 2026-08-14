class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        s = "balloon"
        h = {}
        needed = {}
        res = []
        for letter in text:
            if letter in s:
                h[letter] = h.get(letter, 0) + 1
        for l in s:
            needed[l] = needed.get(l,0) + 1
        print(needed)
        print(h)
        for char in s:
            if char in h and char in needed:
               res.append(h[char]//needed[char])
            else:
                return 0
        return min(res)


        
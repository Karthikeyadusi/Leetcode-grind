class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ft = {}
        for letter in t:
            ft[letter] = ft.get(letter,0) + 1
        left = 0
        h = {}
        lenght = 0
        formed = 0
        best_starting = left
        best_ending = 0
        best = len(s) + 1
        for right in range(0, len(s)):
            adding = s[right]
            h[adding] = h.get(adding, 0) + 1
            lenght+=1
            if ft.get(adding, 0) == h[adding]:
                formed+=1
            while formed==len(ft):
                if lenght < best:
                    best_starting = left
                    best_ending = lenght
                    best = lenght
                h[s[left]]-=1
                if h[s[left]] < ft.get(s[left], 0):
                    formed-=1
                if h[s[left]]==0:
                    del h[s[left]]
                left+=1
                lenght-=1
        if best == len(s) + 1:
            return ""
        else:
            return s[best_starting:best_starting+best]

            
                
                

        
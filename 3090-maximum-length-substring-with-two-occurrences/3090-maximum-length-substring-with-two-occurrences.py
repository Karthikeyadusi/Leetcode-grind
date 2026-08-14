class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left = 0
        best = 0
        h = {}
        for right in range(0,len(s)):
            adding = s[right]
            h[adding] = h.get(adding, 0) + 1
            while h[adding] >2:
                removing = s[left]
                h[removing]-=1
                if h[removing] == 0:
                    del h[removing]
                left+=1
            best = max(best, right-left+1)
        return best
            
        
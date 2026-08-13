class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        h = {}
        left = 0
        best = 0
        for right in range(0,len(s)):
            adding = s[right]
            h[adding] = h.get(adding, 0) + 1
            while h[adding] > 1:
                h[s[left]]-=1
                if h[s[left]] == 0:
                    del h[s[left]]
                left+=1
            best = max(best, right-left+1)
        return best
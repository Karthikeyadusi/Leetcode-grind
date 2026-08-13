class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        h = {}
        left = 0
        best = 0
        for right in range(0,len(fruits)):
            adding = fruits[right]
            h[adding] = h.get(adding, 0) + 1
            while len(h) > 2:
                h[fruits[left]]-=1
                if h[fruits[left]] == 0:
                    del h[fruits[left]]
                left+=1
            best = max(best, right-left+1)
        return best        
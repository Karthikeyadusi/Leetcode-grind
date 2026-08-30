class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        children = sorted(g)
        cookies = sorted(s)
        output = 0
        i = 0
        j = 0
        while i < len(cookies) and j < len(children):
            if cookies[i] >= children[j]:
                i+=1
                j+=1
                output+=1
            else:
                i+=1
        return output





        
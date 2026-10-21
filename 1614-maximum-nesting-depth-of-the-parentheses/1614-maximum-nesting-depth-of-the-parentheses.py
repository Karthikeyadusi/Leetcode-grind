class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_depth=0
        for letter in s:
            if letter == "(":
                depth+=1
            max_depth = max(depth, max_depth)
            if letter == ")":
                depth-=1
        return max_depth

            
        
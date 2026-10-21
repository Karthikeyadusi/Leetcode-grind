class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        res = [""] * len(s)
        ans = ""
        for i,letter in enumerate(s):
            res[indices[i]] = letter
        print(res) 
        ans = "".join(res)
        return ans       
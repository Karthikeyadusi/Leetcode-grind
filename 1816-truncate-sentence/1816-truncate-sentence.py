class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        words = s.split(" ")
        print(words)
        desired = words[:k]
        ans = " ".join(desired)
        return ans      
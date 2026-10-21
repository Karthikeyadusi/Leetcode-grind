class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        r1 = ""
        for word in word1:
            r1+=word
        r2 = ""
        for word in word2:
            r2+=word
        return r1 == r2
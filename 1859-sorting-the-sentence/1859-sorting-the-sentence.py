class Solution:
    def sortSentence(self, s: str) -> str:
        string = s.split(" ")
        result = [""] * len(string)
        ans = ""
        for i, word in enumerate(string):
            position = int(word[-1])
            actual = word[:-1]
            result[position-1] = actual
        ans = " ".join(result)
        return ans

        
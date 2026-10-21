class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        words = set(sentence)
        return len(words) == 26
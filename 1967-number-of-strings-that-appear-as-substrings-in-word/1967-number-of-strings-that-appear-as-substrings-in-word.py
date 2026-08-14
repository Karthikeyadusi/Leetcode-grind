class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        def checksubstring(w, word):
            if w in word:
                return True
            return False
        count= 0
        for w in patterns:
            if checksubstring(w, word):
                count+=1
        return count


        
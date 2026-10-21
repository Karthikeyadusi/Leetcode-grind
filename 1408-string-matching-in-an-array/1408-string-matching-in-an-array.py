class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        result = []
        def isSubstring(w1, w2):
            if w1 in w2:
                return w1
            elif w2 in w1:
                return w2
            else:
                return
        for i in range(0,len(words)):
            for j in range(i+1, len(words)):
                ans = isSubstring(words[i], words[j])
                if ans is not None and ans not in result:
                    result.append(ans)
        return result
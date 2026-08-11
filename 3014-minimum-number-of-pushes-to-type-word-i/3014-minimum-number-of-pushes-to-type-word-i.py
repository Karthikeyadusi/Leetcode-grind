class Solution:
    def minimumPushes(self, word: str) -> int: 
        pushes = 0
        for i in range(1,len(word)+1):
            if i <= 8:
                pushes+=1
            elif 8 < i <=16:
                pushes+=2
            elif 17 <= i <=24:
                pushes+=3
            else:
                pushes+=4
        return pushes
        
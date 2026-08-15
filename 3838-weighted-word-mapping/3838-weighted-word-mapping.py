class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        mapping = {}
        weight = {}
        result = ""
        s = "abcdefghijklmnopqrstuvwxyz"
        i = 0
        for l in s:
            weight[l] = weight.get(l, 0) + weights[i]
            i+=1
        # print(h)
        rev = s[::-1]
        for i in range(0,len(rev)):
            mapping[i] = rev[i]
        # print(mapping)
        for word in words:
            total = 0
            for letter in word:
                total += weight.get(letter, 0)
            total = total % 26
            req = mapping.get(total, "")
            result+=req
        return result
                
        
        

        

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}
        for letter1 in s:
            hashmap1[letter1] = hashmap1.get(letter1,0) + 1
        for letter2 in t:
            hashmap2[letter2] = hashmap2.get(letter2,0) + 1
        return hashmap1 == hashmap2
        
        
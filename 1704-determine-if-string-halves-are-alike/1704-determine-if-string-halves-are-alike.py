class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def countVowels(word):
            w = word.lower()
            count = 0
            vowels = "aeiou"
            for letter in w:
                if letter in vowels:
                    count+=1
            return count
        n = len(s)//2
        word1 = s[:n]
        word2 = s[n:]
        return countVowels(word1) == countVowels(word2)
        

        
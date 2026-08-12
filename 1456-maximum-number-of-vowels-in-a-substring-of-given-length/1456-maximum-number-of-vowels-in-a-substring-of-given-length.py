class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        def count_vowels(total):
            count = 0
            vowels = "aeiou"
            for t in total:
                if t in vowels:
                    count+=1
            return count
        vowels = "aeiou"
        count = count_vowels((s[0:k]))
        max_count = count
        for i in range(1,len(s)-k+1):
            if s[i-1] in vowels:
                count-=1
            if s[i+k-1] in vowels:
                count+=1
            if count > max_count:
                max_count = count
        return max_count
        
        
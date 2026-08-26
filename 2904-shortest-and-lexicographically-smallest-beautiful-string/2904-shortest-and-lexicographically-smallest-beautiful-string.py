class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:


        #my version of optimal solution

        ones = []
        best = float("inf")
        start = 0
        for i in range(len(s)):
            if s[i] == "1":
                ones.append(i)
        for i in range(len(ones)-k+1):
            lenght = ones[i+k-1] - ones[i] +1
            if lenght < best:
                best = lenght
                start = i
            if best == lenght:
                str1 = s[ones[start]: ones[start+k-1]+1]
                str2 = s[ones[i] : ones[i+k-1]+1]
                if str2<str1:
                    best = lenght
                    start  = i
        if best == float("inf"):
            return ""
        return s[ones[start] : ones[start+k-1] + 1]
                
            

        

        #optimal solution
        # ones = []
        # candidate = ""
        # best = ""
        # for i in range(len(s)):
        #     if s[i] == '1':
        #         ones.append(i)
        # for i in range(len(ones)-k+1):
        #     candidate = s[ones[i] : ones[i+k-1]+1]
        #     if (best == "" or len(candidate) < len(best) or (len(candidate) == len(best) and candidate < best)):
        #         best = candidate
        # return best
























        #mysolution

        # left = 0
        # best = ""
        # count = 0
        # indices = []
        # while left < len(s) and s[left] == "0":
        #     left+=1
        # for right in range(left,len(s)):
        #     adding = s[right]
        #     indices.append(right)
        #     if adding == "1":
        #         count+=1
        #     while count > k:
        #         if s[left] == "1":
        #             count-=1
        #         indices.remove(left)
        #         left+=1
        #     if count == k:
        #         first = 0
        #         last = len(indices) - 1
        #         while first<=last and s[indices[first]] == "0":
        #             first+=1
        #         while last>=first and s[indices[last]] == "0":
        #             last-=1
        #         candidate = ""
        #         for i in range(first, last+1):
        #             candidate+=s[indices[i]]
        #         if best == "" or len(candidate)< len(best):
        #             best = candidate
        #         elif len(candidate) == len(best) and candidate < best:
        #             best = candidate
        # return best
        
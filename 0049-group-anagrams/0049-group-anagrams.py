class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapper = {}

        for s in strs:
            temp = "".join(sorted(s))
            if temp in mapper:
                mapper[temp].append(s)
            else:
                mapper[temp] = [s]
        res = []
        for key in mapper:
            res.append(mapper[key])
        return res
class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        if ruleKey == "color":
            check = 1
        elif ruleKey == "type":
            check = 0
        else:
            check = 2
        count = 0
        for i in range(0,len(items)):
            if items[i][check] == ruleValue:
                count+=1
        return count
        

        
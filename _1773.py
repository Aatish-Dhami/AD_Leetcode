class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        rulekeys = ['type', 'color', 'name']
        indx = rulekeys.index(ruleKey)

        count = 0
        for item in items:
            if item[indx] == ruleValue:
                count += 1
        return count

items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
c1 = Solution()
x = c1.countMatches(items, ruleKey,ruleValue)
print(x)
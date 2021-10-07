class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lst = []
        temp = ''
        for x in s:
            if x not in temp:
                temp += x
            else:
                lst.append(len(temp))
                temp = temp[temp.index(x)+1:] + x
        lst.append(len(temp))
        return max(lst)

c1 = Solution()
x = c1.lengthOfLongestSubstring("sjkfvbjkfsjkbfskjf")
print(x)
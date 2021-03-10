class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        temp = ""
        for i in range(len(s)):
            for j in range(len(indices)):
                if indices[j] == i:
                    temp = temp + s[j]
        return temp

    def restoreStrings(self, s: str, indices: list[int]) -> str:
        temp = ['a'] * len(s)
        for i in range(len(s)):
            temp[indices[i]] = s[i]
        temp_str = "".join(temp)
        return temp_str

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
c1 = Solution()
x = c1.restoreStrings(s, indices)
print(x)
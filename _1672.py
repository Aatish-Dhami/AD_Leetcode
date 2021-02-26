class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        temp = 0
        highest = 0
        for i in range(len(accounts)):
            t = i
            for j in range(len(accounts[i])):
                temp = temp + accounts[i][j]
            if temp > highest:
                highest = temp
            temp = 0
        return highest

inp = [[2,8,7],[7,1,3],[1,9,5]]
c1 = Solution()
x = c1.maximumWealth(inp)
print(x)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        for stn in stones:
            if stn in jewels:
                count +=1
        return count

jewels = "z"
stones = "ZZ"
c1 = Solution()
x = c1.numJewelsInStones(jewels, stones)
print(x)
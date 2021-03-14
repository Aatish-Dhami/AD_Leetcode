class Solution:
    def decode(self, encoded: list[int], first: int) -> list[int]:
        temp = [first, encoded[0] ^ first]
        i = 1
        while i < len(encoded):
            temp.append(encoded[i] ^ temp[len(temp) - 1])
            i +=1
        return temp


n = [1,2,3]
first = 1
c1 = Solution()
x = c1.decode(n, first)
print(x)
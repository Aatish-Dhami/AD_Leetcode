class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        temp = []
        for i in range(n):
            temp.append(nums[i])
            temp.append(nums[i+n])
        return temp
n = 4
inp = [1,2,3,4,4,3,2,1]
c1 = Solution()
x = c1.shuffle(inp,n)
print(x)
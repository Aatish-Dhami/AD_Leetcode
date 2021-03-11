class Solution:
    def decompressRLElist(self, nums: list[int]) -> list[int]:
        temp = []
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                temp.append(nums[i+1])
        return temp

n = [1,1,2,3]
c1 = Solution()
x = c1.decompressRLElist(n)
print(x)
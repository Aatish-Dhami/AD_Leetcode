class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        total = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    total += 1
        return total

inp = [1,2,3]
c1 = Solution()
x = c1.numIdenticalPairs(inp)
print(x)

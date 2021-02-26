class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        temp = []
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            temp.append(sum)
        return(temp)

arr = [1,1,1,1,1,1]
c1 = Solution()
x = c1.runningSum(arr)
print(x)
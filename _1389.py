class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        target.append(nums[0])
        for i in range(1, len(nums)):
            if index[i] == len(target):
                target.append(nums[i])
            elif index[i] < len(target):
                j = len(target) - 1
                target.append(target[j])
                j-=1
                while j >= index[i]:
                    target[j+1] = target[j]
                    j-=1
                target[j+1] = nums[i]
        return target


nums = [1,2,3,4,0]
index = [0,1,2,3,0]
c1 = Solution()
x = c1.createTargetArray(nums, index)
print(x)
class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        temp = []
        for num in nums:
            count = 0
            for i in range(len(nums)):
                if nums[i] < num:
                    count += 1
            temp.append(count)
        return temp


nums = [7,7,7,7]
c1 = Solution()
x = c1.smallerNumbersThanCurrent(nums)
print(x)
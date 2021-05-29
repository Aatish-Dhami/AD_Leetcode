class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = []
        temp = 0

        for i in range(n):
            nums.append(start + 2*i)
        print(nums)

        for number in nums:
            temp = temp ^ number
        return temp

c1 = Solution()
x = c1.xorOperation(10,5)
print(x)
                

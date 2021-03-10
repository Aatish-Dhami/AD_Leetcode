class Solution:
    def numberOfSteps (self, num: int) -> int:
        count = 0
        if num < 1:
            print("Invalid input")
        while num != 0:
            if num % 2 != 0:
                num -= 1
                count += 1
            else:
                num /= 2
                count += 1
        return count

num = 123
c1 = Solution()
x = c1.numberOfSteps(num)
print(x)
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        product = 1
        while n > 0:
            sum = sum + (n % 10)
            product = product * (n % 10)
            n //= 10
        return (product - sum)

n = 4421
c1 = Solution()
x = c1.subtractProductAndSum(n)
print(x)
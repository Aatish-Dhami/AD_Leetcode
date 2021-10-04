class Solution:
    def isPalindrome(self, x: int) -> bool:
        temp = 0
        original = x
        while(x>0):
            temp = (temp*10) + x%10
            x = x//10
        if temp == original:
            return True


c1 = Solution()
x = c1.isPalindrome(121)
print(x)
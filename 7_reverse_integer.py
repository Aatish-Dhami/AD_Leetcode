class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        flag = 0
        if x<0:
            flag = 1
            x = x*-1
        while x!=0:
            rev = (rev*10) + (x%10)
            x = x//10
        if rev<-2147483648 or rev>2147483647:
            return 0
        if flag == 0:
            return rev
        else:
            return -rev



c1 = Solution()
x = c1.reverse(1534236469)
print(x)
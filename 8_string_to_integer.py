class Solution:
    def myAtoi(self, s: str) -> int:
        signflag = None
        dflag = None
        numb = 0
        for char in s:
            if char == " " and signflag == None and dflag == None:
                continue
            else:
                if char == '-' and dflag == None and signflag == None:
                    signflag = 0
                elif char == '+' and dflag == None and signflag == None:
                    signflag = 1
                elif char in ['0','1','2','3','4','5','6','7','8','9']:
                    numb = numb*10 + int(char)
                    dflag = 1
                else:
                    break

        if (signflag == 1 or signflag == None) and numb < 2147483648:
            return numb
        elif (signflag == 1 or signflag == None) and numb > 2147483647:
            return 2147483647
        if signflag == 0 and -numb < -2147483648:
            return -2147483648
        else:
            return -numb


c1 = Solution()
x = c1.myAtoi("0   123")
print(x)
class Solution:
    def interpret(self, command: str) -> str:
        temp = ""
        i = 0
        while i < len(command):
            if command[i] == "G":
                temp = temp + "G"
                i+=1
            elif i < len(command) and command[i+1] == ")":
                temp = temp + "o"
                i+=2
            else:
                temp = temp + "al"
                i+=4
        return temp

n = "(al)G(al)()()G"
c1 = Solution()
x = c1.interpret(n)
print(x)
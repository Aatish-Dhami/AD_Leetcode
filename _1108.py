class Solution_1108:
    def defangIPaddr(self, address: str) -> str:
        len_adr = len((address))
        for i in range(len_adr):
            if address[(len_adr-1) - i] == ".":
                temp = address[((len_adr-1)-i) + 1:]
                address = address[:len_adr-i-1] + "[.]" + temp
        return address

ipadr = "255.100.50.0"
c1 = Solution_1108()
x = c1.defangIPaddr(ipadr)
print(x)
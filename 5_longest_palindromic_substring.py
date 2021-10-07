class Solution:
    def longestPalindrome(self, s: str) -> str:
        pal = ''
        i = 0
        # for i in range((len(s)//2)):
        while True:
            temp = s[i:i+len(pal)]
            j = i+len(pal)
            while True:
                if temp[0:] == temp[::-1] and len(temp) > len(pal):
                    pal = temp
                if j>=len(s):
                    break
                temp+=s[j]
                j = j+1
            i=i+1
            if i>(len(s)):
                break
        return pal
            # for j in range(i+len(pal), len(s)):
            #     if temp[0:] == temp[::-1]:
            #         pal = temp
            #     temp+=s[j]
                # else:
                #     temp = temp[1:] + s[i]
                # else:
            #     temp = temp[temp.index(char)+1:]


c1 = Solution()
x = c1.longestPalindrome("jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel")
print(x)
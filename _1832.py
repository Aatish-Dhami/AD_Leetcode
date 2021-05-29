class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        list_of_alph = "abcdefghijklmnopqrstuvwxyz"
        for alph in list_of_alph:
            if alph not in sentence.casefold():
                return False
        else:
            return True

c1 = Solution()
x = c1.checkIfPangram("anmt")
print(x)
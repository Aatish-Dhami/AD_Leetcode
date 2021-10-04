class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        temp1 = ""
        temp2 = ""

        for word in word1:
            temp1 = temp1 + word
        for word in word2:
            temp2 = temp2 + word
        if temp2 == temp1:
            return True
        else:
            return False

c1 = Solution()
w1 = ["a", "cc"]
w2 = ["ab", "c"]
x = c1.arrayStringsAreEqual(w1, w2)
print(x)
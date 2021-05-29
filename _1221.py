class Solution:
    def balancedStringSplit(self, s: str) -> int:
        countt = 0
        rr = ""
        ss = ""
        for chr in s:
            if chr == "R":
                rr = rr + "R"
            elif chr == "L":
                ss = ss + "L"
            if rr.count("R") == ss.count("L"):
                countt += 1
                rr = ""
                ss = ""
        return countt

c1 = Solution()
x = c1.balancedStringSplit("RLRRLLRLRL")
print(x)
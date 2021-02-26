class Solution_1431:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        highest = max(candies)
        temp = []
        for i in range(0, len(candies)):
            temp.append(candies[i] + extraCandies >= highest)
        return temp

extraCandies = 10  # random.randint(1,50)
candies = [12, 1, 12]

c1 = Solution_1431()
print(c1.kidsWithCandies(candies, extraCandies))


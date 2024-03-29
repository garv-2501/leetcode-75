class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        tempCandies = []
        for i in range(len(candies)):
            tempCandies.append(candies[i] + extraCandies)

        result = []
        highestNumber = max(candies)
        for i in range(len(tempCandies)):
            if tempCandies[i] >= highestNumber:
                result.append(True)
            else:
                result.append(False)

        return result
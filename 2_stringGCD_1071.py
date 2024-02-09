import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if (str1 + str2 == str2 + str1):
            x = math.gcd(len(str1), len(str2))
            return str1[:x]
        
        
trial = Solution()
print(trial.gcdOfStrings("AB", "ABABAB"))
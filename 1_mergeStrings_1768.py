class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        output = ""
        count = 0
        
        for i in range(min(len(word1), len(word2))):
            count += 1
            output += word1[i]
            output += word2[i]
            
        output += word1[count:] + word2[count:]
        return output

        
# make an object from Solutions and run findbiggerstring
trial = Solution()

print(trial.mergeAlternately("abccccccccc" , "xyzdddddd"))


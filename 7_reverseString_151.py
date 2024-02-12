class Solution:
    def reverseWords(self, s: str) -> str:
        inputString = s.strip() + " "
        words = []
        currentWord = ""
        for i in range(len(inputString)):
            if inputString[i] != " ":
                currentWord += inputString[i]
            else:
                if (currentWord != ""):
                    words.append(currentWord)
                currentWord = ""
                
        words.reverse()
        outputString = " ".join(words)
        return outputString
        
trial = Solution()

print(trial.reverseWords("    hello     this is me    "))
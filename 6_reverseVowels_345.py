class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        inputString = []
        vowelsInString = []
        
        for i in range(len(s)):
            inputString.append(s[i])
            if s[i] in vowels:
                vowelsInString.append(s[i])
                
        counter = -1            
        for i in range(len(inputString)):
            if inputString[i] in vowels:
                inputString[i] = vowelsInString[counter]
                counter -= 1
                
        outputString = "".join(inputString)
        return outputString
        
trial = Solution()

print(trial.reverseVowels("hello"))
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        counterS = 0
        indexS = 0
        if len(s) < 1:
            return True
        if len(s) == 1:
            if s in t:
                return True
            else:
                return False
        for i in range(len(t)):
            if t[i] == s[indexS]:
                if indexS == len(s):
                    return True
                print(s[indexS], " is there")
                indexS += 1
                
        if indexS == len(s):
            return True
        return False
    
trial = Solution()
print(trial.isSubsequence("b", "adbdksdfsc"))
                
                
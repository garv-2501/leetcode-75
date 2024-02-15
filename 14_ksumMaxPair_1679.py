class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:

        foundNumberFreq = {}
        pairCounter = 0
        
        for num in nums:
            if num in foundNumberFreq:
                foundNumberFreq[num] += 1
            else:
                foundNumberFreq[num] = 1
            
        for num in nums:
            complement = k - num
            
            if num in foundNumberFreq and foundNumberFreq[num] > 0:
                foundNumberFreq[num] -= 1
                if complement in foundNumberFreq and foundNumberFreq[complement] > 0:
                    print("Found complement: ", num, " ", complement)
                    pairCounter += 1
                    foundNumberFreq[complement] -= 1
                    print(foundNumberFreq)
                else:
                    foundNumberFreq[num] += 1
        
        return pairCounter
    
nums1 = [3,1,3,4,3]
k1 = 6

trial = Solution()
print(trial.maxOperations(nums1, k1))
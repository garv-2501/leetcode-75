from cmath import inf


class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        
        first, second = inf, inf

        for num in nums:
            if first >=num:
                first = num
            elif second >= num:
                second = num
            else:
                return True
            
        return False
    
trial = Solution()

print(trial.increasingTriplet([1,2,3,4]))
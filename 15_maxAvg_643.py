class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        
        window = sum(nums[:k])
        maxAvg = window / k

        for i in range(len(nums) - k):
            window = window - nums[i] + nums[i + k]
            print("window: ", window, " from - to :", nums[i])
            maxAvg = max(maxAvg, (window/k))
        
        return maxAvg


trial = Solution()
print(trial.findMaxAverage([1,12,-5,-6,50,3], 4))
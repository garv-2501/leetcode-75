class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = 0
        index = 0
        if len(nums) > 1:
            while True:
                if nums[index] == 0:
                    nums.pop(index)
                    nums.append(0)
                    index -= 1
                    counter += 1
                else:
                    index += 1
                    counter += 1

                if counter >= len(nums)-1:
                    break
        return nums

        
trial = Solution()
print(trial.moveZeroes([2,1, 1]))
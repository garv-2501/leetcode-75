class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        if len(nums) < 3:
            return False
        
        shortMemory_longerNum = nums[0]
        longMemory_longerNum = []

        counter = 0
        counterMemory = []
        for i in range(1, len(nums)):
            if nums[i] > shortMemory_longerNum:
                shortMemory_longerNum = nums[i]
                counter += 1
                if (counter == 2):
                    return True
            else:
                longMemory_longerNum.append(shortMemory_longerNum)
                shortMemory_longerNum = nums[i]
                counterMemory.append(counter)
                counter = 0
                
        for i in range(1, len(nums)):
            if nums[i] in longMemory_longerNum:
                print(nums[i], " in there")
                for j in range(i, len(nums)):
                    if nums[i] < nums[j]:
                        print(nums[j], " is bigger")
                        if counterMemory[longMemory_longerNum.index(nums[i])] == 1:
                            print("True!! Found one", nums[j])
                            return True
                
        return False
        print("longTermMemory: ", longMemory_longerNum)
        print("counterMemory: ", counterMemory)
                
trial = Solution()
print(trial.increasingTriplet([20,100,10,12,5,9, 1, 20]))
print("")

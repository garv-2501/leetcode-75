class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        temp_flowerbed = flowerbed

        counter = 0
        
        if len(flowerbed) >= 3:
            if temp_flowerbed[0] == 0 and temp_flowerbed[1] == 0:
                counter +=1
                temp_flowerbed[0] = 1
            if temp_flowerbed[-1] == 0 and temp_flowerbed[-2] == 0:
                counter +=1
                temp_flowerbed[-1] = 1
            
            for i in range(1, len(flowerbed)-1):
                if temp_flowerbed[i-1] == 0 and temp_flowerbed[i] == 0 and temp_flowerbed[i+1] == 0:
                    temp_flowerbed[i] = 1
                    counter += 1
        elif len(flowerbed) == 2:
            if temp_flowerbed[0] == 0 and temp_flowerbed[1] == 0:
                counter = 1
                temp_flowerbed[0] == 1
        elif len(flowerbed) == 1:
            if temp_flowerbed[0] == 0:
                counter = 1
                temp_flowerbed[0] == 1
                
                
        print(counter)
        if n > counter:
            return False
        else:
            return True
            
            
            
trial = Solution()
flowerbed1 = [1]
print(trial.canPlaceFlowers(flowerbed1, 0))
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = 1
        productsArray = []
        zeroCount = 0
        for number in nums:
            if number != 0:
                product = product * number
            else:
                zeroCount += 1
            
        # if there are more than 2 zeros
        if zeroCount >= 2:
            productsArray = [0] * len(nums)
            return productsArray
        
        if zeroCount == 1:
            for number in nums:
                if number != 0:
                    productsArray.append(0)
                else:
                    productsArray.append(product)  
                    
        if zeroCount == 0:
            for number in nums:
                productsArray.append(int(product/number))
            
        return productsArray
    
trial = Solution()
print(trial.productExceptSelf([2,3,4]))
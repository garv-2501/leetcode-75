from cmath import inf


class Solution:
    def maxArea(self, height: list[int]) -> int:

        pointerLeft = 0
        pointerRight = len(height) - 1
        
        maxAreaFound = -inf;
        
        while pointerLeft < pointerRight:
            shorterOne = min(height[pointerLeft], height[pointerRight])
            area = shorterOne * (pointerRight - pointerLeft)
            print("New area! between: ", height[pointerLeft], " and ", height[pointerRight], " Area: ", area)
            if area > maxAreaFound:
                maxAreaFound = area
                
                
            if height[pointerLeft] > height[pointerRight]:
                pointerRight -= 1
            else:
                pointerLeft += 1
                
        return maxAreaFound
        
trial = Solution()
print(trial.maxArea([1,8,6,2,50,4,80,3,7]))
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights)-1
        
        maxWater = 0
        while l < r:
            h = min(heights[l], heights[r])
            length = r - l
            water = h* length
            if(maxWater < water):
                maxWater = water
                print(maxWater, h , length)
            
            if(heights[l] > heights[r]):
                r-=1
            elif heights[l] < heights[r]:
                l+=1
            else:
                r-=1
                
        return maxWater

        
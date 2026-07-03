class Solution:
    def trap(self, height: List[int]) -> int:


        # If we calculate the max heights for each positions on the left and on the right
        # for each position, we can find how much water can be trapped 

        # BUT THERE IS A CHEEKIER WAY
        # What we can do is create two pointers and variables maxLeft and maxRight
        # change the pointer only if one of the max heights is smaller or equal than the other
        # So we know that the max height on the other side is always bigger or equal
        # Thus We can only care about the smaller maxValue

        l, r = 0, len(height) - 1
        water = 0
        maxLeft, maxRight = height[l], height[r]

        while l < r:
            if maxLeft < maxRight: 
                l += 1
                maxLeft = max(maxLeft, height[l])
                water += maxLeft - height[l] 
                # this will not be negative because if the height is smaller
                # than the current height we are replacing the leftMax with 
                # the current height which will be zero
            else:
                r-=1
                maxRight = max(maxRight, height[r])
                water += maxRight - height[r] # Same logic as above

        return water

        
            

        
        
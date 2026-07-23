#Trapping Rain Water Problem using Two Pointer Approach
'''Algorithm:
1. search for the tallest wall to the left of current_height
2. search for the tallest wall to the right of current_height
3. water_level = min(height[left],height[right])
4. water at current index= water_level - current_height
'''

'''Mathematical Algorithm
totalWater = 0

For every index i:

    Find tallest wall on the left

    Find tallest wall on the right

    water = min(leftMax, rightMax) - height[i]

    Add water to total
'''

heights=[0,1,0,2,1,0,1,3,2,1,2,1]
def trapping_rain_water(heights):
    left=0
    right=len(heights)-1
    leftMax=heights[left]
    rightMax=heights[right]
    water=0
    while left<right:
        
        if leftMax<=rightMax:
            leftMax=max(leftMax,heights[left])
            water+=leftMax-heights[left]
            left+=1 #The water at the left pointer is fully determined.

        else:
            rightMax=max(rightMax,heights[right])
            water+=rightMax-heights[right]
            right-=1 #The water at the right pointer is fully determined.

    return water
print(trapping_rain_water(heights))

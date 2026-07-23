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


'''
Given an array height of n non-negative integers where each element 
represents the height of a bar in a histogram-like structure.
These bars are placed next to each other, width of each bar is 1 unit.
Task is to calculate how much water can be trapped between these bars 
after the rain

Input :- an array height of n non-negative integers
Output :- count integer which is the calculated amount of water trapped between the bars

Time Complexity :- O(n)
Space Complexity :- O(1)
'''
def trapping_rain_water(height):
    if len(height)<=1:
            return 0

    left = 0
    right = len(height)-1
    count = 0

    left_max = 0
    right_max = 0

    while left<=right:
        if height[left]<height[right]:
            if height[left]>=left_max:
                left_max = height[left]
            else:
                count += (left_max-height[left])

            left += 1

        else:
            if height[right]>=right_max:
                right_max = height[right]
            else:
                count += (right_max - height[right])

            right -= 1

    return count

#test case 1
arr = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapping_rain_water(arr))

#test case 2
arr = [4, 2, 0, 3, 2, 5]
print(trapping_rain_water(arr))

#test case 3
arr = [1, 1, 1]
print(trapping_rain_water(arr))

#test case 4
arr = [5]
print(trapping_rain_water(arr))

#test case 5
arr = [2,0,2]
print(trapping_rain_water(arr))
#!/usr/local/bin/python

def max_volume(height):
    length = 0
    end = len(height) -1 
    max_area = 0
    while length < end :
        if height[length] > height[end]:
            area = height[end] * ( end - length)
            end -= 1
        else:
            area = height[length] * ( end - length)
            length += 1
        max_area = max(area , max_area)
     return max_area 
           

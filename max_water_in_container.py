class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        lptr = 0
        rptr = len(height) - 1
        while lptr <= rptr:
            min_height = min(height[lptr],height[rptr])
            max_water = max(max_water, min_height*(rptr - lptr))
            if height[lptr] < height[rptr]:
                lptr += 1
            else:
                rptr -= 1
        return max_water

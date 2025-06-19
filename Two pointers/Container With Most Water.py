class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left and right
        l, r = 0, len(heights) - 1
        max_area = 0

        while l < r: # Move towards the lower boundary
            l_max, r_max = heights[l], heights[r]

            area = min(l_max, r_max) * (r - l)
            max_area = max(max_area, area)

            if l_max < r_max:
                l += 1
            else:
                r -= 1
                
        return max_area
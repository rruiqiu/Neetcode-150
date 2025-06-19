class Solution:
    def trap(self, height: List[int]) -> int:
        # increment the counts

        l, r = 0, len(height) - 1
        l_max, r_max = height[l], height[r]
        water_area = 0

        while l < r:
            # Move towards the higher boundary
            if l_max < r_max:
                l += 1
                #check if the new l_max
                if height[l] < l_max:
                    water_area += l_max - height[l]
                else:
                    l_max = height[l]
            else:
                r -= 1
                if height[r] < r_max:
                    water_area += r_max - height[r]
                else:
                    r_max = height[r]
        
        return water_area



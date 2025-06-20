class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # heigh, max_width, max_height

        max_area = 0
        stack = []  # keep track of the areas

        for r, height in enumerate(heights):
            # if the curr height is smaller than previous, pop the stack
            curr = r
            while stack and height < stack[-1][0]:
                l_height, l = stack.pop()
                max_area = max(max_area, (curr - l) * l_height)
                r = l
                #
            stack.append((height, r))
        # and also process the end of stack
        r = len(heights)
        while stack:
            l_height, l = stack.pop()
            max_area = max(max_area, (r - l) * l_height)
        return max_area

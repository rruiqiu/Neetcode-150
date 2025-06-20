class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Mono stack with the index stored

        stack = []
        res = [0] * len(temperatures)

        for r, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                val, l = stack.pop()
                res[l] = r - l

            stack.append((temp, r))
        return res

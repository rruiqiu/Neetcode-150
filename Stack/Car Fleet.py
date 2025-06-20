class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # position = [4,1,0,7], speed = [2,2,1,1]

        # 8 2 1 7
        pos_speed = []
        for i in range(len(position)):
            pos_speed.append((position[i], speed[i]))

        pos_speed.sort(reverse=True)

        stack = []  # maintain the number of overlapped fleets
        for i in range(len(pos_speed)):
            time_take = (target - pos_speed[i][0]) / pos_speed[i][1]  # Float
            if (
                stack and time_take > stack[-1]
            ):  # copmare every element, cuz the stack is in increasing order, so we don't need to worry about the order, always compare with the current largest, if over means a new fleet found
                stack.append(time_take)
            if i == 0:
                stack.append(time_take)
                continue
        return len(stack)

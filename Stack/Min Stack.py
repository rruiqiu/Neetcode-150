class MinStack:
    def __init__(self):
        self.stack = []
        # Keep a record of each value with the min

    def push(self, val: int) -> None:
        if self.stack:
            min_value = self.getMin()
            if min_value < val:
                self.stack.append((val, min_value))
            else:
                self.stack.append((val, val))
        else:
            self.stack.append((val, val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        print(self.stack)
        return self.stack[-1][1]

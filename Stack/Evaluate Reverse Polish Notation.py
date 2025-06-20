class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            # assume the stack would always be true when encounter a symbol
            if token in ("+", "-", "*", "/"):
                right = stack.pop()
                left = stack.pop()
                if token == "+":
                    stack.append(int(left) + int(right))
                elif token == "-":
                    stack.append(int(left) - int(right))
                elif token == "*":
                    stack.append(int(left) * int(right))
                elif token == "/":
                    stack.append(int(left) / int(right))
            else:
                stack.append(token)

        return int(stack[-1])

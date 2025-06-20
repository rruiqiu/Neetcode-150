class Solution:
    def isValid(self, s: str) -> bool:
        # Use Stack
        stack = []

        for char in s:
            # If closing bracket
            if stack and char in (")", "}", "]"):
                top = stack.pop()
                if top == "(" and char == ")":
                    continue
                elif top == "{" and char == "}":
                    continue
                elif top == "[" and char == "]":
                    continue
                else:
                    # Not a valid match
                    return False
            stack.append(char)
        if stack:
            return False
        return True

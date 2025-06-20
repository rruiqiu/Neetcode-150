class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Backtracking with stack
        stack = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            # openN should alwasy be greater than closeN
            if openN < n:  # 2 conditions
                stack.append("(")
                backtrack(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                backtrack(openN, closeN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

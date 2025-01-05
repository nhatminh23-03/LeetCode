class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = []
        res = []
        def backtracking(openP, closeP):
            if openP == closeP == n:
                res.append("".join(stack))
                return

            if openP < n:
                stack.append("(")
                backtracking(openP + 1, closeP)
                stack.pop()
            if closeP < openP:
                stack.append(")")
                backtracking(openP, closeP + 1)
                stack.pop()

        backtracking(0,0)
        return res

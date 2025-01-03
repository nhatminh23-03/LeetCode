class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            else:
                if not stack:
                    return False
                topStack = stack.pop()
                if (c == ")" and not topStack == "(") or (c == "]" and not topStack == "[") or (c == "}" and not topStack == "{"):
                    return False 
        return len(stack) == 0
                    

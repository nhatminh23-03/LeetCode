class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dict_c = {")": "(", "}": "{", "]": "["}
        for c in s:
            if c in dict_c:
                if stack and stack[-1] == dict_c[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
        

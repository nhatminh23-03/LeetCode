class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        # stack = []
        # for token in tokens:
        #     if token.isdigit() or (token[0] == '-' and len(token) > 1):
        #         stack.append(int(token))
        #     else:
        #         if len(stack) < 2:
        #             raise ValueError("Insufficient operands for operator")
        #         val1 = stack.pop()
        #         val2 = stack.pop()

        #         if token == "+":
        #             stack.append(val2 + val1)
        #         elif token == "-":
        #             stack.append(val2 - val1)
        #         elif token == "*":
        #             stack.append(val2 * val1)
        #         elif token == "/":
        #             stack.append(int(float(val2) / val1))  # Integer division
        # return stack[0]

        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(float(b) / a))
            else:
                stack.append(int(token))
        return stack[0]


                
                
            
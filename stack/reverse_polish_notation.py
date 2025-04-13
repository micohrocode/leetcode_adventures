class Solution(object):
    def evalRPN(self, tokens):
        stack = []

        for c in tokens:
            # evaluate operations in order
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop() , stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop() , stack.pop()
                stack.append(int(float(b) / a))
            else:
                # add number to stack
                stack.append(int(c))
        
        return stack[0]
        
def isValid(self, s):
    stack = []
    closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

    for c in s:
        if c in closeToOpen:
            # check to see if the opening bracket is in the stack
            if stack and stack[-1] == closeToOpen[c]:
                # remove the opening bracket
                stack.pop()
            else:
                # else it cannot be valid
                return False
        else:
            # add the opening to the stack
            stack.append(c)

    return True if not stack else False
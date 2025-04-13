class MinStack(object):

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        # add value to the stack
        self.stack.append(val)
        # check the new min
        val = min(val, self.min_stack[-1] if self.min_stack else val)
        # add to the min stack
        self.min_stack.append(val)
        

    def pop(self):
        # remove the values from the stacks
        self.stack.pop()
        self.min_stack.pop()
        

    def top(self):
        # view the top of the stack
        return self.stack[-1]
        

    def getMin(self):
        # view the current min of the stack
        return self.min_stack[-1]
        

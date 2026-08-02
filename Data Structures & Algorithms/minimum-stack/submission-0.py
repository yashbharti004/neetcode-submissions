class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
            
        
    def pop(self) -> None:
        if not self.stack:
            print("stack underflow")
        else:
            return self.stack.pop()
        

    def top(self) -> int:
        if not self.stack:
            print("stack is empty")
        else:
            return self.stack[-1]
        

    def getMin(self) -> int:
        if not self.stack:
            print("stack is empty")
        else:
            mini = self.stack[0]
            for i in self.stack:
                if mini > i:
                    mini = i
            return mini

class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minimumOrder = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimumOrder:
            self.minimumOrder.append(min(self.minimumOrder[-1], val))
        else:
            self.minimumOrder.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minimumOrder.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimumOrder[-1]
        

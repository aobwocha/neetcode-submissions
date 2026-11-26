class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min is None:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            self.min = min(self.min, val)

    def pop(self) -> None:
        res = self.stack.pop()

        if not self.stack:
            self.min = None
        elif res < 0:
            self.min -= res

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min
        
        return self.stack[-1] + self.min 

    def getMin(self) -> int:
        return self.min

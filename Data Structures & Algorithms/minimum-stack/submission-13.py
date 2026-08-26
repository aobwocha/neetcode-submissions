class MinStack:

    def __init__(self):
        self.stack = list()
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
        if res < 0:
            self.min -= res
        
        if not self.stack:
            self.min = None

    def top(self) -> int:
        res = self.stack[-1]
        if res > 0:
            return res + self.min
        else:
            return self.min

    def getMin(self) -> int:
        return self.min        

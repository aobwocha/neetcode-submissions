class MinStack:

    def __init__(self):
        self.stack = []
        self.min_num = None

    def push(self, val: int) -> None:
        if self.min_num is None:
            self.stack.append(0)
            self.min_num = val
        else:
            self.stack.append(val - self.min_num)
            self.min_num = min(self.min_num, val)

    def pop(self) -> None:
        res = self.stack.pop()
        if res < 0:
            self.min_num -= res
        
        if not self.stack:
            self.min_num = None

    def top(self) -> int:
        if self.stack[-1] < 0:
            return self.min_num
        else:
            return self.stack[-1] + self.min_num

    def getMin(self) -> int:
        return self.min_num

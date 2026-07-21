class MinStack:
    '''
    So we want to store a value and the minimum value at the instance it is stored

    We can store the value as the diff between itself and the min at storage
        [ele, ele, ele]
           ^   ^    ^
         min1 min2 min2
    
    If we need to pop, we need to check if what we stored was positive, to know if it is curr min
    If not, just pop regularly but if it is negative, we know that it's the curr min and we can calc prev min
    And keep repeating
    '''
    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            self.stack.append(val - self.min)
            if val < self.min:
                self.min = val

    def pop(self) -> None:
        pop = self.stack.pop()

        if pop < 0:
            self.min -= pop

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return self.min + top
        else:
            return self.min

    def getMin(self) -> int:
        return self.min

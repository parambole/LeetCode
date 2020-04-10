class MinStack:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stackA = []
        self.stackB = []
        

    def push(self, x: int) -> None:
        self.stackA.append(x)
        if len(self.stackB) == 0:
            self.stackB.append(x)
        elif x <= self.stackB[-1]:
            self.stackB.append(x)
        

    def pop(self) -> None:
        x = self.stackA.pop()
        if x == self.stackB[-1]:
            self.stackB.pop()
        

    def top(self) -> int:
        return self.stackA[-1]
        

    def getMin(self) -> int:
        if len(self.stackB) == 0:
            return []
        return self.stackB[-1]

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

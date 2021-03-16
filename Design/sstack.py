class SStack:
    
    def __init__(self, parent=None,level=0,value=-1):
        self.parent = parent
        self.level = level
        self.value = value
        
        
    def push(self, value):
        return SStack(self, self.level + 1, value)
    
    def pop(self):
        return self.parent if self.parent else self
    
    def size(self):
        return self.level
    

p0 = SStack()  #returns a new instance of SStack with elements {}
p1 = p0.push(1); # returns a new instance of SStack with elements {1}
p2 = p1.push(2); # return a new instance of SStack with elements {1,2}
p3 = p1.pop(); # returns a new instance of SStack with elements {}
print(p2.size()) # returns size = 2
print(p1.size()) # returns size = 1
print(p3.size())
    

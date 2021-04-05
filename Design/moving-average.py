import collections
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque([])
        self.size = size
        self.sum = 0

    def next(self, val: int) -> float:
        
        self.q.append(val)
        self.sum += val
        
        if len(self.q) > self.size:
            rem_val = self.q.popleft()
            
            self.sum -= rem_val
            
        return self.sum / len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

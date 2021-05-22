class MyCalendarThree:
    
    """
    The intuition of this question is very similar to meeting rooms
    
    So what mattes is when meetings start and when they end you need to maintain the sorted order for that
    
    And you neeed to have two arrays which can maintain that. 
    
    BUT 
    
    You can also do it USIGN a hashmap which is basically merging the sorted list. SMART ain't in
    
    THE CORE logic is:
    
    A meeting can occupy the first meeting room that is getting over THAT IS MAIn
    
    
    
    
    """

    def __init__(self):
        
        self.delta = collections.Counter()
        

    def book(self, start: int, end: int) -> int:
        
        self.delta[start] += 1
        self.delta[end] -= 1
        
        
        active , ans = 0, 0
        
        # Need to do this as we don't have treeMap in python
        for x in sorted(self.delta):
            active += self.delta[x]
            ans = max(active, ans)
            
        return ans
        


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)

# class StockSpanner:

#     def __init__(self):
#         self.List = []
        

#     def next(self, price: int) -> int:
#         self.List.append(price)
#         count = 0
#         for i in range(len(self.List) - 1, -1, -1):
#             if self.List[i] <= price:
#                 count += 1
#             else:
#                 break
#         return count


class StockSpanner:

    def __init__(self):
        self.List = []
        self.span = []

    def next(self, price: int) -> int:
        self.List.append(price)
        
        n = len(self.List)
        idx = n - 2
        if n == 1:
            self.span.append(1)
        else:
            
            while idx >= 0 and self.List[idx] <= price:
                idx -= self.span[idx]

            self.span.append((n -1) - idx)
        return self.span[-1]
        
        
        
            
            

    
    
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

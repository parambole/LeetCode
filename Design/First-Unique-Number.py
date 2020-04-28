import collections

class DLinkedList:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None
        
        
class FirstUnique:

    def __init__(self, nums: List[int]):
        
        self.dic = {}
        self.head = DLinkedList(-1)
        self.tail = DLinkedList(-1)
                
        self.head.next = self.tail
        self.tail.prev = self.head
        
        for num in nums:
            self.add(num)
            
        
    def showFirstUnique(self) -> int:
        return self.head.next.value
        

    def add(self, value: int) -> None:
        if not value in self.dic:
            
            node = DLinkedList(value)
            self.dic[value] = node
            
            prev = self.tail.prev
            
            prev.next = node
            
            node.prev = prev
            
            node.next = self.tail
            
            self.tail.prev = node
            
        else:
            
            # During multiple delete
            
            if self.dic[value]:
                node = self.dic[value]

                Next = node.next
                Prev = node.prev

                Prev.next = Next
                Next.prev = Prev
                self.dic[value] = None

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)

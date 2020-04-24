class DLinkedList:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DLinkedList(0,0)
        self.tail = DLinkedList(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.currCap = 0
        self.dic = {}
        
        
    
    def removeFromPos(self, node):
        Next = node.next
        Prev = node.prev
        Prev.next = Next
        Next.prev = Prev
        
    def moveToHead(self, node):
        
        
        Next = self.head.next
        
        self.head.next = node
        node.prev = self.head
        
        node.next = Next
        Next.prev = node
    
    def removeLRU(self):
        Prev = self.tail.prev
        # MAde this mistake. See this again
        self.removeFromPos(Prev)
        del self.dic[Prev.key]
        self.currCap -= 1
        

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.removeFromPos(node)
            self.moveToHead(node)
            return node.value
        else:
            return -1
        
        

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            node = self.dic[key]
            node.value = value
            self.removeFromPos(node)
            self.moveToHead(node)
        else:
            node = DLinkedList(key, value)
            self.dic[key] = node
            self.moveToHead(node)
            self.currCap += 1
        
        if self.currCap > self.capacity:
            self.removeLRU()
            

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

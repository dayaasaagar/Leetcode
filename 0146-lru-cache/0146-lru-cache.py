

class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):

        self.cache = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next= self.tail
        self.tail.prev = self.head
    
    def add_to_front(self,node):

        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    def remove(self,node):

        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add_to_front(node)
            return node.value
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key,value)
        self.add_to_front(node)
        self.cache[key]=node

        if len(self.cache)>self.capacity:
            lru = self.tail.prev
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
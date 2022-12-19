from LinkedList import LinkedList

class Stack_L:
    def __init__(self):
        self._L = list()        # Composition: the Stack_L class has a List
    
    def push(self,item):
        self._L.append(item)
    
    def pop(self):
        return self._L.pop()

class Stack_LL:
    def __init__(self):
        self._LL = LinkedList() # Composition: the Stack_LL class has a Linked List
    
    def push(self, item):
        self._LL.add_first(item)
        
    def pop(self):
        return self._LL.remove_first()

class Queue_L:
    def __init__(self):
        self._L = list()
    
    def enqueue(self, item):
        self._L.append(item)
    
    def dequeue(self):
        return self._L.pop(0)

class Queue_LL:
    def __init__(self):
        self._LL= LinkedList()
    
    def enqueue(self, item):
        self._LL.add_first(item)
    
    def dequeue(self):
        return self._LL.remove_last()

if __name__ == '__main__':
    
    ##########Test Stack_L##########
    LStack1 = Stack_L()
    for i in range(10):
        LStack1.push(i*3)
        for i in range(9,-1,-1):
            assert LStack1.pop() == i*3
    ##########Test Stack_LL#########
    LLStack1 = Stack_LL()
    for i in range(8):
        LLStack1.push(i*2)
        for i in range(7, -1, -1):
            assert LLStack1.pop() == i*2
    ##########Test Queue_L##########
    queue1 = Queue_L()
    for i in range(5):
        queue1.enqueue(i*4)
        for i in range(5):
            assert queue1.dequeue() == i*4
    ##########Test Queue_LL#########
    queue2 = Queue_LL()
    for i in range(6):
        queue2.enqueue(i*3)
        for i in range(6):
            assert queue2.dequeue() == i*3
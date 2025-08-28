class Node(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class Queue: 
    def __init__(self): 
        self.head = None 
        self.tail = None 
        self.count = 0 

    def enqueue(self, data): 
        new_node = Node(data, None, None) 
        if self.head == None: 
            self.head = new_node 
            self.tail = self.head 
        else: 
            new_node.prev = self.tail 
            self.tail.next = new_node 
            self.tail = new_node 

        self.count += 1 


    def dequeue(self): 
        if self.count == 1: 
            self.count -= 1 
            self.head = None 
            self.tail = None 
        elif self.count > 1: 
            self.head = self.head.next 
            self.head.prev = None 
        elif self.count <1:
            print("Queue is empty")
        self.count -= 1 

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("")

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next


q= Queue()
q.enqueue('Pedro')
q.enqueue('José')
q.enqueue('Maria')

print("Fila Inicial:")
q.traverse()

print(q.count)

print(q.dequeue())

print(q.count)
print("Agora a fila é:")
q.traverse()
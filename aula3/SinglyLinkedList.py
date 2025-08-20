'''
Acesse: 
https://github.com/PacktPublishing/Hands-On-Data-Structures-and-Algorithms-with-Python-Third-Edition/tree/main/Chapter04
'''

class Node:
    def __init__ (self, data=None):
        self.data = data 
        self.next = None


class SinglyLinkedList:
    def __init__ (self):
        self.tail = None
        self.head = None
        self.size = 0

    def iter(self):
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node 
            self.tail = node

    def append_at_a_location(self, data, index): 
        current = self.head 
        prev = self.head 
        node = Node(data)
        count = 1
        while current:
            if count == 1:        
                node.next = current
                self.head = node
                print(count)
                return
            elif index == index:
                node.next = current 
                prev.next = node
                return
            count += 1
            prev = current
            current = current.next
        if count < index:
            print("The list has less number of elements")
          
    def search(self, data):
        for node in self.iter():
            if data == node:
                return True
        return False
    
    def size(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def delete_first_node (self):
        current = self.head  
        if self.head is None:
              print("No data element to delete")
        elif current == self.head:
              self.head = current.next  
    
    def delete_last_node (self):  
        current = self.head  
        prev = self.head  
        while current: 
            if current.next is None: 
                prev.next = current.next  
                self.size -= 1 
            prev = current 
            current = current.next
    
    def delete(self, data):
        current = self.head 
        prev = self.head 
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next 
                else:
                    prev.next = current.next 
                self.size -= 1
                return
            prev = current
            current = current.next
    
    def clear(self):
        self.tail = None
        self.head = None
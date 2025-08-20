from DoublyLinkedList import DoublyLinkedList

words = DoublyLinkedList()
words.append('egg')
words.append('ham')
words.append('spam')

print("Items in doubly linked list before append")
current = words.head
while current:
    print(current.data)
    current = current.next
    
words.append_at_start('book')

print("Items in doubly linked list after append")
current = words.head
while current:
    print(current.data)
    current = current.next


words.append('book')

print("Items in doubly linked list after adding element at end.")
current = words.head
while current:
    print(current.data)
    current = current.next
    


words.append_at_a_location('ham')
print("Doubly linked list after adding an element after word \"ham\" in the list.")
current = words.head
while current:
    print(current.data)
    current = current.next


words = DoublyLinkedList()  
words.append('egg')  
words.append('ham')  
words.append('spam') 


words.contains("ham")  
words.contains("ham2") 
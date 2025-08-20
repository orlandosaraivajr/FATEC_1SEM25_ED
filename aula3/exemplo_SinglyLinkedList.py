from SinglyLinkedList import SinglyLinkedList, Node


lista = SinglyLinkedList()

# Inserindo elementos na lista
lista.append(10)
lista.append(20)
lista.append(30)
lista.append(40)

# Exibindo os elementos da lista
print("Lista após inserções (10, 20, 30, 40):")
current = lista.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Procurando elementos
print("\nProcurando pelo valor 20:", lista.search(20))
print("Procurando pelo valor 50:", lista.search(50))

# Deletando o primeiro nó
lista.delete_first_node()
print("\nLista após deletar o primeiro nó (10 removido):")
current = lista.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Deletando o último nó
lista.delete_last_node()
print("\nLista após deletar o último nó (40 removido):")
current = lista.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Deletando um elemento específico
lista.delete(20)
print("\nLista após deletar o nó com valor 20:")
current = lista.head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

# Limpando a lista
lista.clear()
print("\nLista após clear():", lista.head)

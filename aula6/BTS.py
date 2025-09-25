class Node:
    def __init__(self, data: str):
        self.data = data
        self.right_child = None
        self.left_child = None

class Tree:
    def __init__(self):
        self.root_node = None

    def insert(self, data: str):
        node = Node(data)
        if self.root_node is None:
            self.root_node = node
            return self.root_node
        else:
            current = self.root_node
            parent = None
            while True:
                parent = current
                if node.data.lower() < parent.data.lower():  # comparação em ordem alfabética
                    current = current.left_child
                    if current is None:
                        parent.left_child = node
                        return self.root_node
                else:
                    current = current.right_child
                    if current is None:
                        parent.right_child = node
                        return self.root_node

    def inorder(self, root_node): 
        current = root_node 
        if current is None: 
            return 
        self.inorder(current.left_child) 
        print(current.data) 
        self.inorder(current.right_child)

    def search(self, data: str):
        current = self.root_node
        while True:
            if current is None:
                print(f"Nome '{data}' não encontrado")
                return None
            elif current.data.lower() == data.lower():
                print(f"Nome encontrado: {data}")
                return data
            elif current.data.lower() > data.lower():
                current = current.left_child
            else:
                current = current.right_child

    def find_min(self):  
        current = self.root_node  
        while current.left_child:  
            current = current.left_child  
        return current.data          
    
    def find_max(self):  
        current = self.root_node  
        while current.right_child:  
            current = current.right_child  
        return current.data


# ----------------------------
# Exemplo de uso
# ----------------------------
tree = Tree()
tree.insert("Maria")
tree.insert("João")
tree.insert("Ana")
tree.insert("Carlos")
tree.insert("Beatriz")

print("Ordem alfabética (inorder):")
tree.inorder(tree.root_node)

print("\nBusca:")
tree.search("Carlos")
tree.search("Pedro")

print("\nMenor nome:", tree.find_min())
print("Maior nome:", tree.find_max())

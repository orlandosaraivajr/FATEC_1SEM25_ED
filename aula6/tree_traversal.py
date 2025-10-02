class Node: 
    def __init__(self, data): 
        self.data = data 
        self.right_child = None 
        self.left_child = None 


n1 = Node("pai")   
n2 = Node("filho esquerda")  
n3 = Node("filho direita")  
n4 = Node("neto esquerda")

n1.left_child = n2 
n1.right_child = n3 
n2.left_child = n4 

current = n1 
while current: 
        print(current.data) 
        current = current.left_child 

print("\n" )

def inorder(root_node): 
        current = root_node 
        if current is None: 
            return 
        inorder(current.left_child) 
        print(current.data) 
        inorder(current.right_child) 

def preorder(root_node): 
        current = root_node 
        if current is None: 
            return 
        print(current.data) 
        preorder(current.left_child) 
        preorder(current.right_child) 


def postorder(root_node): 
        current = root_node 
        if current is None: 
            return 
        postorder(current.left_child) 
        postorder(current.right_child) 
        print(current.data)

print("EM ORDEM\n" )
inorder(n1)
print("\n" )
print("PRÉ ORDEM\n" )
preorder(n1)
print("\n" )
print("POS ORDEM\n" )
postorder(n1)

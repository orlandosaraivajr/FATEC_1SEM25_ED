from collections import deque 

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



def level_order_traversal(root_node): 
    list_of_nodes = [] 
    traversal_queue = deque([root_node]) 
    while len(traversal_queue) > 0:
        node = traversal_queue.popleft() 
        list_of_nodes.append(node.data) 
        if node.left_child: 
            traversal_queue.append(node.left_child) 
            if node.right_child: 
                traversal_queue.append(node.right_child) 
    return list_of_nodes 



print(level_order_traversal(n1))

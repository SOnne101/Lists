class Node:
    def __init__(self,val):
        self.val = val # Set the node value
        self.next = None # The pointer initially points to nothing

    def traverse(self):
        node = self # Start from the head node
        while node != None: #C heck if there is a node
            print(node.val) # Print the node value
            node = node.next # Move on to the next node


class DoublyNode:
    def __init__(self, val):
        self.val = val # Set the node value
        self.next = None # The pointer initially points to nothing
        self.prev = None # The pointer initially points to nothing

    def traverse(self):
        node = self # Start from the head node
        while node != None: # Chech if there is a node
            print(node.val) # Print the node value
            node = node.next # Move on to the next node
    
    def backward(self):
        node = self # Start from the head node
        while node != None: # Chech if there is a node
            print(node.val) # Print the node value
            # Using a try/except in case we link a doubly node with a regular node
            try:
                node = node.prev # Move to previouse node
            except:
                print('node does not have a prev')
                return
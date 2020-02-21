# Imports
from nodes import Node, DoublyNode 

# Instanciate three node with some values
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

# Link the node together
node1.next = node2
node2.next = node3

# Traversing our list
node1.traverse()

print('-----------------------------------------------------------')

# Instanciate three new double node with some new values
node4 = DoublyNode(4)
node5 = DoublyNode(5)
node6 = DoublyNode(6)

# Link the double nodes together
node4.next = node5
node5.next = node6

# Link the double nodes together backwards
node4.prev = node3
node5.prev = node4
node6.prev = node5

# Treversing the double nodes, first forward and the then backwards
node4.traverse()
node6.backward()

print('-----------------------------------------------------------')

# Link both types of nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

# Traversing all the nodes forwards and backwards
node1.traverse()
node6.backward()
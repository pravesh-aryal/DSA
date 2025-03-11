class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = None 

    def __str__(self):
        return "I am a NODE str representation"

Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)
Node4 = Node(4)
Node5 = Node(5)


Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5

#printing the list
currentNode = Node1
while currentNode != None:
    print(currentNode.data)
    currentNode = currentNode.next



"""
Node1 (data, pointerToNextNode), Node 2 (data, pointerToNextNode), Last Node (data, NULL)
"""

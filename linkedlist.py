class Node:

    def __init__(self, data, nextPointer = None):
        self.data = data
        self.nextPointer = None


    def __str__(self):
        return "I am a NODE str representation"

Node1 = Node(1)
Node2 = Node(1, id(Node1))
print(id(Node1))
print(Node1)

"""
Node1 (data, pointerToNextNode), Node 2 (data, pointerToNextNode), Last Node (data, NULL)
"""

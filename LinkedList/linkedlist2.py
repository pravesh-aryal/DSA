class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"({self.data})"
        

class LinkedList:
    
    def __init__(self):
        self.head = None

    def insertNodeAtEnd(self, node):
    #this runs only once the if below 
        if (self.head == None):
            self.head = node
            #
            return
        
        currentNode = self.head
        while(currentNode.next != None):
            currentNode = currentNode.next
        
        currentNode.next = node

    def __str__(self):
        #shows what the current list looks like
        currentNode = self.head
        strFormat = ""
        while (currentNode != None):
            strFormat += str(currentNode) + " --> " 
            currentNode = currentNode.next
            
        return strFormat + "None"
    
    def insertNodeAtBeginning(self, node):
        #if the list is empty
        if (self.head == None):
            self.head = node
            return

        headNode = self.head
        #we need to set the node as headNode and change headNode to second node on the list.
        node.next = headNode
        self.head = node


linkedList1 = LinkedList()

for i in range(0, 5):
    linkedList1.insertNodeAtBeginning(Node(i+1))

#the LL should handle creating nodes and setting up next's automatically.
for i in range(0, 10):
    linkedList1.insertNodeAtEnd(Node(i+1))

print(linkedList1)

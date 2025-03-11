class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = None

    def __str__(self):
        return f"({self.data})"
        

class LinkedList:
    
    def __init__(self):
        self.head = None

    def addNode(self, node):
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


linkedList1 = LinkedList()

#the LL should handle creating nodes and setting up next's automatically.
linkedList1.addNode(Node(1))
linkedList1.addNode(Node(2))
linkedList1.addNode(Node(3))
linkedList1.addNode(Node(4))
linkedList1.addNode(Node(5))


print(linkedList1)

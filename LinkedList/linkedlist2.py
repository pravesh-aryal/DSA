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
        if self.head == None:
            return "The linkedlist is empty" 

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

    
    def deleteNodeByReference(self, node):
        if (self.head == None):
            self.__str__()
            return

        currentNode = self.head
        #if node to delete is head.
        if (node == self.head):
            #set the second node as head.
            self.head = self.head.next
            print(self.__str__())
            return
        previousNode = None
        while (currentNode != None):

            if currentNode == node:
                previousNode.next = currentNode.next
            previousNode = currentNode
            currentNode = currentNode.next

        print(self.__str__())
        
linkedList1 = LinkedList()
#
#for i in range(0, 5):
#    linkedList1.insertNodeAtBeginning(Node(i+1))
#
##the LL should handle creating nodes and setting up next's automatically.
#for i in range(0, 10):
#    linkedList1.insertNodeAtEnd(Node(i+1))
#

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

linkedList1.insertNodeAtEnd(node1)
linkedList1.insertNodeAtEnd(node2)
linkedList1.insertNodeAtEnd(node3)
linkedList1.insertNodeAtEnd(node4)

linkedList1.deleteNodeByReference(node1)
linkedList1.deleteNodeByReference(node2)
linkedList1.deleteNodeByReference(node4)
linkedList1.deleteNodeByReference(node3)
linkedList1.deleteNodeByReference(node1)





#priority queue = heap
#we are doing min heap here
class PriorityQueue:

    def __init__(self, pq_size):
        self.pq_size = pq_size
        self.q = [None] * (self.pq_size+1) #capacity of heap i.e underlying array representing heap
        self.n = 0 #how many positions in the queue are actually in use

    def insert(self, item):
        if (self.n >= self.pq_size):
            print("Queue used more than allocated")
        else:
            self.n += 1
            self.q[self.n] = item
            self.bubbleUp(self.n)

    def bubbleUp(self, n):
        if (n == 1):
            return
        #get parent using current n
        parentIndex = n // 2
        childIndex = n
        if (self.q[parentIndex] <= self.q[childIndex]):
            return
        
        #else swap
        self.q[parentIndex], self.q[childIndex] = self.q[childIndex], self.q[parentIndex]

        #recursive calls with floor(n) i.e parent index until base case to bubble up
        # up means parent index
        self.bubbleUp(parentIndex)


    def getParent(self):
        return 

    def getLeftChild(self):
        pass

    def getRightChild(self):
        pass

pq = PriorityQueue(10)

pq.insert(1)
pq.insert(3)
pq.insert(5)
pq.insert(7)
pq.insert(9)
pq.insert(2)
print(pq.q)

from Node import Node

class LinkedList(object):

    def __init__(self) -> None:
        self.head = None
        self.counter = 0     

    # O(N)
    def traverseList(self):
        actualNode = self.head

        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextnode

    # O(1)    
    def insertStart(self, data):
        self.counter += 1
        newNode = Node(data)

        if not self.head:
            self.head = newNode
        else:
            newNode.nextnode = self.head
            self.head = newNode

    # O(1) instead of O(N)
    def size(self):
        return self.counter

    # O(N) !!
    def insertEnd(self, data):
        if self.head is None:
            self.insertStart(data)
            return
        
        self.counter += 1

        newNode = Node(data)
        actualNode = self.head

        while actualNode.nextnode is not None:
            actualNode = actualNode.nextnode
        
        actualNode.nextnode = newNode

    # O(N) or O(1) if we're removing the first element
    def remove(self, data):

        self.counter -= 1

        if self.head:
            if data == self.head.data:
                self.head = self.head.nextnode
            else:
                self.head.remove(data, self.head) 
# Creating a doubly circular linked list

class Node:

    def  __init__(self, value=None) -> None:
        self.next = None
        self.prev = None
        self.value = value


class CircularDoublyLinkedList:
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next 

    def createDCLL(self, nodeValue):
        """
        Initiates the Doubly Circular Linked List with  the given value
        If the list isn't empty, function does nothing
        """
        if self.head:
            print("There are pre-existing elements in this list")
            return
        else:
            node = Node(nodeValue)
            node.next = node
            node.prev = node
            self.head = node
            self.tail = node
    
    def insert(self, nodeValue, location):
        """
        Inserts a value in the given list based on given parameters: nodeValue, location
        location == 0: Value is inserted at the beginning
        location == -1: Value is inserted at the end
        location > highest index possible for inserting, function doesn't insert anything
        """
        if not self.head:
            if location in (0, -1):
                self.createDCLL(nodeValue=nodeValue)
                return
        newNode = Node(nodeValue)    
        if location == 0:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode
        elif location == -1:
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.tail = newNode
        else:
            i = 0
            tempNode = self.head
            while i < location - 1:
                tempNode = tempNode.next
                i += 1
                if tempNode == self.tail and i == location - 1:
                    self.insert(nodeValue=nodeValue, location=-1)
                    return
                if tempNode == self.tail and i < location - 1:
                    return
            nextNode = tempNode.next
            newNode.prev =  tempNode
            newNode.next = nextNode
            tempNode.next = newNode
            nextNode.prev = newNode

    def traverse(self):
        """
        Traverse through the list
        Prints out the list values with spacing between them
        """
        node = self.head
        while node:
            print(node.value, end=" ")
            if node.next == self.head:
                break
            node = node.next
        print()

    def checkNode(self, nodeValue):
        """
        Return bool value indicating whether a node with given value exists
        Returns False if the list is empty
        """
        if not self.head:
            return False
        tempNode = self.head
        while tempNode.value != nodeValue:
            if tempNode == self.tail:
                return False
            tempNode = tempNode.next
        return True

    def findNode(self, location):
        """
        Returns value of Node at specified location parameter
        if location value > number of nodes, function returns None
        if list is empty, function returns None
        """
        if not self.head:
            return None
        i = 0
        node = self.head
        while i < location:
            if node == self.tail:
                return None
            node = node.next
            i += 1
        return node.value

    def deleteHead(self):
        """
        if list is empty, does nothing
        Deletes the first element in the list
        """
        if not self.head:
            return
        else:
            if self.head == self.tail:
                self.head.next = None
                self.tail.prev = None
                self.head = None
                self.tail = None
            else:
                nextNode = self.head.next
                nextNode.prev = self.tail
                self.head = nextNode
                self.tail.next = nextNode
    
    def deleteTail(self):
        """
        if list is empty, does nothing
        Deletes the last element in the list
        """
        if not self.head:
            return
        else:
            if self.head == self.tail:
                self.deleteHead()
            else:
                prevNode = self.tail.prev
                prevNode.next = self.head
                self.head.prev = prevNode
                self.tail = prevNode


    def removeNode(self, nodeValue):
        """
        if list is empty, does nothing
        if nodeValue not in the list, does nothing
        """
        if not self.checkNode(nodeValue=nodeValue):
            return
        else:
            if self.head.value == nodeValue:
                self.deleteHead()
            elif self.tail.value == nodeValue:
                self.deleteTail()
            else:            
                tempNode = self.head
                while tempNode.value != nodeValue:
                    tempNode = tempNode.next
                prevNode = tempNode.prev
                nextNode = tempNode.next
                prevNode.next = nextNode
                nextNode.prev = prevNode
        
    def deleteNode(self, location):
        """
        if list is empty,does nothing
        if location = -1, deletes last element
        if location > number of elements, does nothing
        """
        if not self.head:
            return
        if location == 0:
            return self.deleteHead()
        if location == -1:
            return self.deleteTail()
        i = 0
        tempNode = self.head
        while i < location:
            i += 1
            tempNode = tempNode.next
            if tempNode == self.tail and i < location:
                return
            if tempNode == self.tail and i == location:
                return self.deleteTail()

        nextNode = tempNode.next
        prevNode = tempNode.prev
        prevNode.next = nextNode
        nextNode.prev = prevNode

    def deleteEntireList(self):
        """
        Deletes the entire list components
        """
        self.head.prev = None
        self.tail.next = None
        self.head = None
        self.tail = None


# Try
circulardll = CircularDoublyLinkedList()
print([node.value for node in circulardll])

circulardll.createDCLL(1000)
circulardll.traverse()
print("The head value is {}".format(circulardll.head.value))


[circulardll.insert(i, 0) for i in range(10, -1, -1)]
circulardll.traverse()

circulardll.insert("'at end'", 12)
circulardll.traverse()
print(circulardll.tail.value)

# for node in doublycll:
#     print("The next node of {} is {}".format(node.value, node.next.value))
#     print("The prev node of {} is {}".format(node.value, node.prev.value))

emptycdll = CircularDoublyLinkedList()
emptycdll.insert(10, 0)
emptycdll.insert(100, 0)
emptycdll.insert(100, 0)
print("The node we found is",  emptycdll.findNode(2))
emptycdll.traverse()
print("-"* 40 + "\n")

print(circulardll.findNode(12))
print(circulardll.checkNode("'at end'"))

circulardll.traverse()
circulardll.deleteTail()
print(circulardll.head.prev.value)

circulardll.traverse()
circulardll.removeNode(1000)
circulardll.traverse()

print("-"* 40 + "\n")
circulardll.traverse()
circulardll.deleteNode(11)
circulardll.traverse()

# doublycll.deleteEntireList()
# doublycll.traverse()
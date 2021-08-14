# Creating a Doubly Linked List

class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # Creation of Doubly Linked List
    def createDLL(self, nodeValue):
        if self.head:
            return
        else:
            node = Node(nodeValue)
            node.prev = None
            node.next = None
            self.head = node
            self.tail = node
        return "Double Linked List is created successfully"

    def insert(self, nodeValue, location):
        """
        If the list is empty, this function initializes the list with given value irrespective of location
        location = -1, inserts the value at the end of the List
        location >= index values of the nodes, this function inserts the value at the end of the list 
        location < -1 can give errors. Careful with which locations u want to insert at
        """
        if not self.head:
            self.createDLL(nodeValue=nodeValue)
        else:
            newNode = Node(nodeValue)
            if location == 0:
                newNode.prev = self.head.prev
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.prev = self.tail
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                i = 0
                tempNode = self.head
                while i < location - 1 and tempNode.next:
                    tempNode = tempNode.next
                    i += 1
                if not tempNode.next:
                    self.insert(nodeValue=nodeValue, location=-1)
                    return
                nextNode = tempNode.next
                newNode.next = nextNode
                newNode.prev = tempNode
                nextNode.prev = newNode
                tempNode.next = newNode 

    def traverse(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            node = node.next
        print()
            
    def checkNode(self, nodeValue):
        """Returns Bool values indicating whether the node value is in this list"""
        checkNode = self.head
        while checkNode:
            if checkNode.value == nodeValue:
                return True
            checkNode = checkNode.next
        return False
    
    def searchNode(self, location):
        """Returns None if the location is not in viable range"""
        if not self.head:
            return None
        else:
            node = self.head
            i = 0
            while i < location and node:
                node = node.next
                i += 1
            if not node or location < 0:
                return None
            else:
                return node.value
    
    def deleteFirst(self):
        """Removes the first value in this doubly linked list"""
        if not self.head:
            return
        else:
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                tempNode = self.head.next
                tempNode.prev = None
                self.head = tempNode
    
    def deleteLast(self):
        """Removes the last value in this doubly linked list"""
        if not self.head:
            return
        else:
            if self.head.next == None:
                self.head = None
                self.tail = None
            else:
                prevNode = self.tail.prev
                prevNode.next = None
                self.tail = prevNode
    
    def removeNode(self, nodeValue):
        if not self.checkNode(nodeValue=nodeValue):
            return
        if self.head.value == nodeValue:
            self.deleteFirst()
        elif self.tail.value == nodeValue:
            self.deleteLast()
        else:
            tempNode = self.head
            while tempNode.value != nodeValue:
                tempNode = tempNode.next 
            prevNode = tempNode.prev
            nextNode = tempNode.next
            prevNode.next = nextNode
            nextNode.prev = prevNode

    def deleteNode(self, location):
        if not self.head:
            return
        node = self.head
        if location == 0:
            self.deleteFirst()
        elif location == -1:
            self.deleteLast()
        else:
            i = 0
            while i < location:
                if not node.next:
                    return
                node = node.next
                i += 1
            if not node.next:
                self.deleteLast()
                return
            prevNode = node.prev
            nextNode = node.next
            prevNode.next = nextNode
            nextNode.prev = prevNode
        
    def deleteEntireDLL(self):
        if self.head:
            self.head = None
            self.tail = None
        return "Entire elements in this Doubly linked List has/have been moved to garbage collection"
            
        

# TRY
doublyll = DoublyLinkedList()
doublyll.createDLL(1)
[print(node.value) for node in doublyll]

[doublyll.insert(i, -1) for i in range(2, 11)]
doublyll.insert(0, 0)
# doublyll.insert("Inserting this at 3", 3)
# doublyll.insert("Inserting this at 2", -100)
print([node.value for node in doublyll])

print(doublyll.checkNode(2))
for node in doublyll:
    if node.value == 2:
        print("next value is {}".format(node.next.value))
        print("prev value is {}".format(node.prev.value))

doublyll.traverse()

print("\n" + "*"* 55)
emptydll = DoublyLinkedList()
emptydll.traverse()
emptydll.insert(1000, 1000) # whatever location u give, it initializes the list with given value
print(emptydll.searchNode(0))
print(emptydll.checkNode(1000))
print("*"* 55 + "\n" )

# print(doublyll.searchNode(1))

doublyll.traverse()
doublyll.removeNode(10)
doublyll.traverse()
print("Deleting Node using Index from now" + "\n")
doublyll.deleteNode(1000)
doublyll.traverse()

# Creating random one-element doubly linked list for testing
oneElementdll = DoublyLinkedList()
oneElementdll.createDLL(10)
oneElementdll.traverse()
oneElementdll.deleteNode(0)
oneElementdll.traverse()

print("\n" + "Deleting entire list")
doublyll.deleteEntireDLL()
doublyll.traverse()
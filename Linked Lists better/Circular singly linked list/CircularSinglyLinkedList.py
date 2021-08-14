#   Creating a CircularSinglyLinkedList

class Node:

    def __init__(self, value=None) -> None:
        self.next = None
        self.value = value


class CircularSinglyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self) -> None:
        node = self.head
        while node:
            yield node
            if node.next == self.head:   
                break
            node = node.next

    # Creating a Circular singly linkedlist
    def createCSLL(self, nodeValue):
        node = Node(value=nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The Circular Single LinkedList has been created"

    # Inserting a node in Circular Singly LinkedList
    def insert(self, nodeValue, location):
        if not self.head:
            print('This is an empty Circular singly linked list. So, initializing this list with this value')
            self.createCSLL(nodeValue=nodeValue)
        else:
            newNode = Node(value=nodeValue)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = self.head
            elif location == -1:
                newNode.next = self.head
                self.tail.next = newNode
                self.tail = newNode
            else:
                i = 0
                prevNode = self.head
                while i < location - 1:
                    prevNode = prevNode.next
                    i += 1
                nextNode = prevNode.next
                prevNode.next = newNode
                newNode.next = nextNode
        
    def traverse(self):
        node = self.head
        while node:
            print(node.value, end=" ")
            if node.next == self.head:
                break
            node = node.next
        print()
    
    def searchNode(self, location):
        if not self.head:
            print("This is an empty Circular Singly LinkedList")
        else:
            currentNode = self.head
            i = 0
            while i < location and currentNode.next != self.head:
                currentNode = currentNode.next
                i += 1
            if i != location:
                print("Location value exceeds the number of nodes in the list")
                return
            return currentNode.value

    def checkNode(self, nodeValue):
        tempNode = self.head
        while tempNode:
            if tempNode.value == nodeValue:
                return True
            if tempNode.next == self.head:
                break
            tempNode = tempNode.next
        return False

    def deleteFirst(self):
        if not self.head:
            return
        else:
            if self.head.next == self.head:
                self.head = None
                self.tail.next = self.head
                self.tail = None
            else:
                tempNode = self.head.next
                self.head = tempNode
                self.tail.next = tempNode
    
    def deleteLast(self):
        if not self.head:
            return
        else:
            if self.head.next == self.head:
                self.deleteFirst()
            else:
                tempNode = self.head
                while tempNode.next.next != self.head:
                    tempNode = tempNode.next
                tempNode.next = self.head
                self.tail = tempNode

    def removeNode(self, nodeValue):
        if not self.checkNode(nodeValue=nodeValue):
            print("No such value exists in this Circular LinkedList")
        else:
            if self.head.value == nodeValue:
                self.deleteFirst()
            elif self.tail.value == nodeValue:
                self.deleteLast()
            else:
                prevNode = self.head 
                tempNode = self.head.next
                while tempNode.value != nodeValue:
                    prevNode = prevNode.next
                    tempNode = tempNode.next
                prevNode.next = tempNode.next   

    def deleteNode(self, location):
        if not self.head:
            return
        else:
            if location == 0:
                self.deleteFirst()
            else:
                i = 0
                node = self.head
                while i < location - 1 and node.next.next != self.head:
                    node = node.next
                    i += 1

                if i != location - 1:
                    return
                node.next = node.next.next
            
    def deleteEntireList(self):
        if self.head:
            self.head = None
            self.tail.next = self.head
            self.tail = None
        else:
            print("The list is already empty")

# TEST
circularsll = CircularSinglyLinkedList()
print(circularsll.createCSLL(1))    

print([node.value for node in circularsll])

[circularsll.insert(i, -1) for i in range(2, 5)]

circularsll.insert(0, 0)
circularsll.insert(5, 10)


print([node.value for node in circularsll])


print("\n" + "*" * 10  + "Creating and inserting into an Empty List")
emptycsll = CircularSinglyLinkedList()
print(emptycsll.checkNode(10))
emptycsll.traverse()
emptycsll.searchNode(2)
emptycsll.insert(1000, 1000)
print([node.value for node in emptycsll])
print("*" * 10  + "Done with creating and inserting into an Empty List")
print()

circularsll.traverse()
print(circularsll.searchNode(5))
for i in range(10):
    print(circularsll.checkNode(i), end=", ")
print()

[circularsll.insert(i, -1) for i in range(6, 11)]
circularsll.traverse()
print("- "* 100)
print()


circularsll.traverse()
print("Deleting last Element")
circularsll.deleteLast()
print("Adding 5 as the 5th element")
circularsll.insert(5, 5)
print("Deleting last element again")
circularsll.deleteNode(9)
# [circularsll.deleteNode(i) for i in range(8, 0, -1)]
# [circularsll.deleteNode(i) for i in range(0, 100, 2)]
circularsll.traverse() 

# circularsll.deleteEntireList()
# circularsll.traverse()
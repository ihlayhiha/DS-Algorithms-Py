# Tutor way of inserting nodes into a singlylinkedlist

class Node():

    def __init__(self, value=None) -> None:
        self.next = None
        self.value = value 
    

class SLinkedList():

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # new method for Insertion
    def insert(self, value, location):
        """Add a node to a LinkedList

        Location can be given as -1 if you want to add the element at the end of the LinkedList
        If the Location value > No of nodes in the LinkedList, .insert() method automatically -
        -adds the node at the end of the LinkedList
            
        """
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1: 
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1 and tempNode.next:
                    tempNode = tempNode.next
                    index += 1
                if not tempNode.next:
                    self.insert(value, -1)
                else:
                    newNode.next= tempNode.next
                    tempNode.next = newNode

    def traverse(self):
        if not self.head:
            print("This LinkedList is empty")
        else:
            print([node.value for node in self])

    def search(self, nodeValue):
        node = self.head
        while node:
            if node.value == nodeValue:
                return True
            node = node.next
        return False
    
    def deleteHead(self):
        if not self.head.next:
            self.head = self.tail = None
        else:
            tempNode = self.head.next
            self.head = tempNode

    def deleteTail(self):
        if not self.head.next:
            self.head = self.tail = None
        else:
            prevNode = self.head
            tempNode = self.head.next
            while tempNode.next:
                prevNode = tempNode
                tempNode = tempNode.next
            self.tail = prevNode
            prevNode.next = None

    def deleteNode_val(self, nodeValue):
        if not self.search(nodeValue=nodeValue):
            print("This value doesn't exist in this LinkedList")
        else:
            if self.head.value == nodeValue:
                self.deleteHead()
            elif self.tail.value == nodeValue:
                self.deleteTail()
            else:
                prevNode = self.head
                tempNode = self.head.next
                while tempNode.value != nodeValue:
                    prevNode = tempNode
                    tempNode =  tempNode.next
                prevNode.next = tempNode.next
    
    def deleteNode_loc(self, location):
        """ Removes the node at the given location
        
        location = -1, removes the tail node
        location >= number of nodes, removes the tail node
        location = 0, removes the head node
        
        """
        if location == 0:
            self.deleteHead()
        elif location == -1:
            self.deleteTail()
        else:
            i = 0
            prevNode = self.head
            mainNode = self.head.next
            while i < location - 1 and mainNode.next:
                prevNode = mainNode
                mainNode = mainNode.next
                i += 1
            if not mainNode.next:
                self.deleteTail()
            else:
                prevNode.next = mainNode.next
            




singlyLinkedList = SLinkedList()

# adding integers at the end of the LinkedList
[singlyLinkedList.insert(i, -1) for i in range(5)]
# singlyLinkedList.traverse()

singlyLinkedList.insert(0, 0)
singlyLinkedList.insert(0, 1)
# print([node.value for node in singlyLinkedList])

singlyLinkedList.insert("test at location 5", 5)
# print([node.value for node in singlyLinkedList])

singlyLinkedList.traverse()
print("*"* 55)

anotherLinkedList = SLinkedList()
anotherLinkedList.traverse()

print(singlyLinkedList.search(1))
print(anotherLinkedList.search(10))

print("*" * 66)
singlyLinkedList.deleteTail()
singlyLinkedList.deleteTail()
singlyLinkedList.insert(3, 100)

singlyLinkedList.deleteNode_val('test at location 5')
singlyLinkedList.traverse()

singlyLinkedList.insert(10000, 0)
print(singlyLinkedList.head.value)
singlyLinkedList.traverse()

singlyLinkedList.deleteNode_val(10000)
singlyLinkedList.traverse()

print()
singlyLinkedList.deleteNode_loc(3)
singlyLinkedList.traverse()
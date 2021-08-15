# Creating a linked list for all questions in the interview
from random import randint

class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return str(self.value)
    

class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    def __str__(self) -> str:
        values = [str(node.value) for node in self]
        return " -> ".join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, nodeValue):
        newNode = Node(nodeValue) 
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode 

        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        [self.add(randint(min_value, max_value)) for i in range(n)]
        return self

    def removeNode(self, nodeValue):
        if not self.head:
            return
        if self.head.value == nodeValue:
            self.head = self.head.next
        else:
            tempNode = self.head
            mainNode = self.head.next
            while mainNode.value != nodeValue:
                tempNode = tempNode.next
                mainNode = mainNode.next
            
            tempNode.next = mainNode.next

            

# customLinkedList = LinkedList()
# customLinkedList.generate(10, 100, 1000)
# print(customLinkedList)
# print(len(customLinkedList))


# another = LinkedList()
# another.add("Adding a random string")
# print(another)
# another.generate(5, 0, 20)
# another.add(100)
# another.removeNode(100)
# print(another)
# print(len(another))
# creating a Singly Linked List

class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.next = None


class SLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None


singlyLinkedList = SLinkedList()
node1 = Node(1)
# print(node1.value + 10) 
node2 = Node(3)
# node1.next = node2
# print(node1.next.value)

singlyLinkedList.head = node1
singlyLinkedList.head.next = node2 
singlyLinkedList.tail = node2


# Inserting new node in existing SingleLinkedList

# Adding a node at the start of SinglyLinkedList
atStart = Node(0)
atStart.next = singlyLinkedList.head
singlyLinkedList.head = atStart

garbage = singlyLinkedList.head
while garbage:
    print(garbage.value)
    garbage = garbage.next

# Adding a node at the end of SinglyLinkedList
print()

atEnd = Node(4)
singlyLinkedList.tail.next = atEnd
singlyLinkedList.tail = atEnd

garbage = singlyLinkedList.head
while garbage:
    print(garbage.value)
    garbage = garbage.next


# Adding a node at the middle of SinglyLinkedList at position : 2
print()

position = 2
atRandom = Node(2)

currentNode = singlyLinkedList.head
for i in range(position - 1):
    currentNode = currentNode.next

atRandom.next = currentNode.next
currentNode.next = atRandom


garbage = singlyLinkedList.head
while garbage:
    print(garbage.value)
    garbage = garbage.next


# Adding a node again at the end with value = 5

atEnd = Node(5)
singlyLinkedList.tail.next = atEnd
singlyLinkedList.tail = atEnd

garbage = singlyLinkedList.head
while garbage:
    print(garbage.value)
    garbage = garbage.next


# Adding a node at a random position with value "Inserted"
print()

pos = 4
randPosition = Node(f"Inserted as position {pos} i.e. The {pos + 1}th Node")

currentNode = singlyLinkedList.head
for i in range(pos - 1):
    currentNode = currentNode.next

randPosition.next = currentNode.next
currentNode.next = randPosition

garbage = singlyLinkedList.head
while garbage:
    print(garbage.value)
    garbage = garbage.next


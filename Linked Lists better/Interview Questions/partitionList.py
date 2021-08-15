# Create a partition in LinkedList such that all values less than x come before all values greater than x
from LinkedList import LinkedList, Node
from random  import randint

def partitionValue(ll, x):
    if not ll.head:
        return

    checkNode = ll.head
    while checkNode.next:
        if checkNode.next.value < x:
            tempValue = checkNode.next.value
            checkNode.next = checkNode.next.next

            tempNode = Node(tempValue)
            tempNode.next = ll.head
            ll.head = tempNode
        else:
            checkNode = checkNode.next


    return ll




testPartition = LinkedList()
[testPartition.add(randint(1, 10)) for i in range(10)]
print(testPartition)
print(partitionValue(testPartition, 5))          
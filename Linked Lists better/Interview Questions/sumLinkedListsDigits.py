# 2 numbers represented by a linked list, each node contains the digit and the digits are placed in reverse order, Find sum and write it as a linked list
from LinkedList import LinkedList

def addingDigits(ll1, ll2):

    # using len() function
    size1 = len(ll1)
    size2 = len(ll2)
    node1 = ll1.head
    node2 = ll2.head
    sum = 0
    for i in range(size1):
        sum += (10 ** i) * node1.value
        node1 = node1.next
    
    for i in range(size2):
        sum += (10 ** i) * node2.value
        node2 = node2.next

    print(sum)
    solutionll = LinkedList()
    while sum != 0:
        solutionll.add(sum % 10)
        sum = sum // 10

    return solutionll

    

addTestLL1 = LinkedList()
addTestLL2 = LinkedList()
addTestLL1.add(0)
addTestLL1.add(1)
addTestLL1.add(1)
addTestLL1.add(1)
addTestLL1.add(1)
addTestLL2.add(1)
addTestLL2.add(1)
addTestLL2.add(1)
addTestLL2.add(1)
addTestLL2.add(1)
addTestLL2.add(1)
addTestLL2.add(1)
print(addingDigits(addTestLL1, addTestLL2))
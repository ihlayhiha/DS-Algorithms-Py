# Returning nth to last element
from LinkedList import LinkedList


def nthToLast(ll, n):


    # Using len() function --------------------------------> O(n)
    size = len(ll)
    if n > size or ll.head is None:
        return

    index = len(ll) - n - 1
    i = 0
    node = ll.head
    for i in range(index + 1):
        node = node.next
    return node.value


    # Without using len() function -----------------------> O(n)
    # Basically using a pointer to calculate the size
    # if not ll.head:
    #     return
    # size = 0
    # checkNode = ll.head
    # while checkNode:
    #     size += 1
    #     checkNode = checkNode.next
    
    # checkPoint = size - n
    # point = 0
    # mainNode = ll.head
    # while point < checkPoint:
    #     mainNode = mainNode.next
    #     point += 1
    # return mainNode.value
        
    


checkll = LinkedList()
[checkll.add(i) for i in range(1, 11)]
print(checkll)

print(nthToLast(checkll, 12))
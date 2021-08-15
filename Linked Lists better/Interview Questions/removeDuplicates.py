from LinkedList import Node, LinkedList

def removeDuplicates(unsortedList):

    # Creating a new linked list --------------->O(n)
    # checkList = []
    # for node in unsortedList:
    #     if node.value not in checkList:
    #         checkList.append(node.value)    
    # sortedList = LinkedList()
    # for value in checkList:
    #     sortedList.add(value)
    # return sortedList


    # Using the .removeNode() method------------>O(n**2)
    # checkList = []
    # for node in unsortedList:
    #     if node.value not in checkList:
    #         checkList.append(node.value)
    #     else:
    #         unsortedList.removeNode(node.value)
    # return unsortedList

    # Using While loop-------------------------->O(n)
    # if not unsortedList.head:
    #     return 
    # prevNode = unsortedList.head
    # checkSet = {prevNode.value}
    # while prevNode.next:
    #     if prevNode.next.value in checkSet:
    #         prevNode.next = prevNode.next.next
    #     else:
    #         checkSet.add(prevNode.next.value)
    #         prevNode = prevNode.next
    # return unsortedList
    

    # Without creating a new set--------------->O(n**2)
    if not unsortedList.head:
        return
    node = unsortedList.head
    while node:
        prevNode = node
        while prevNode.next:
            if prevNode.next.value == node.value:
                prevNode.next = prevNode.next.next
            else:
                prevNode = prevNode.next
        node = node.next
    return unsortedList

    


testingLinkedList = LinkedList()
for a in range(10):
    testingLinkedList.add(a)
addingList = [1, 1, 2, 3 ,5]
[testingLinkedList.add(i) for i in addingList]    
print(testingLinkedList)
print(removeDuplicates(testingLinkedList))

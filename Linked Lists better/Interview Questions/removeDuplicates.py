from LinkedList import Node, LinkedList

def removeDuplicates(unsortedList):

    # Creating a new linked list
    # checkList = []
    # for node in unsortedList:
    #     if node.value not in checkList:
    #         checkList.append(node.value)    
    # sortedList = LinkedList()
    # for value in checkList:
    #     sortedList.add(value)
    # return sortedList


    # Using the .removeNode() method
    # checkList = []
    # for node in unsortedList:
    #     if node.value not in checkList:
    #         checkList.append(node.value)
    #     else:
    #         unsortedList.removeNode(node.value)
    # return unsortedList

    # Using a for loop .remove() method


    # using a While loop
    # if not unsortedList.head:
    #     return
    # currentNode = unsortedList.head
    # checkSet = {currentNode.value}
    # while currentNode.next:
    #     if currentNode.next.value in checkSet:
    #         currentNode.next = currentNode.next.next
    #     else:
    #         checkSet.add(currentNode.next.value)
    #         currentNode =  currentNode.next
    # return unsortedList

    
    # Without creating a new buffer list or set

    


unsorted = LinkedList()
for a in range(10):
    unsorted.add(a)
addingList = [1, 1, 2, 3 ,5]
[unsorted.add(i) for i in addingList]    
print(unsorted)
print(removeDuplicates(unsorted))

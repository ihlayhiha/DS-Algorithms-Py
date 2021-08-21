# check if 2 linked lists have an intersection
from LinkedList import LinkedList, Node

def checkIntersection(ll1, ll2):

    if ll1.tail != ll2.tail:
        return False    

    # Using nested loop ---------------> O(mn)
    # for node1 in ll1:
    #     for node2 in ll2:
    #         if node1.next and node2.next:
    #             if node1.next == node2.next:
    #                 return node1.next
    # return False


    # Using len() function ------------> O(m + n)
    len1 = len(ll1)
    len2 = len(ll2)

    shorter = ll1 if len1 < len2 else ll2
    longer = ll1 if len1 > len2 else ll2

    diff  = len(longer) - len(shorter) 
    longerNode = longer.head
    shorterNode = shorter.head

    for i in range(diff):
        longerNode = longerNode.next
    
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode




# Helper addition method to add same Node to both LinkedLists

def addSameNode(ll1, ll2, value):
    tempNode = Node(value=value)
    ll1.tail.next = tempNode
    ll1.tail = tempNode
    ll2.tail.next = tempNode
    ll2.tail = tempNode


ll1 = LinkedList()
ll2 = LinkedList()
ll1.generate(5, 1, 10)
ll2.generate(3, 1, 10)


addSameNode(ll1, ll2, 200)
addSameNode(ll1, ll2, 300)
addSameNode(ll1, ll2, 400)
for node1 in ll1:
    for node2 in ll2:
        if node1 and node2:
            if node1 is node2:
                print(node2, end=", ")
print("\n")
print(ll1)
print(ll2)
print()
print(checkIntersection(ll1, ll2))
# check if 2 linked lists have an intersection
from LinkedList import LinkedList

def checkIntersection(ll1, ll2):

    if not ll1 or not ll2:
        return False
    
    for node1 in ll1:
        for node2 in ll2:
            if node1 == node2:
                return True
    return False


testIntersectionll1 = LinkedList()
testIntersectionll2 = LinkedList()
testIntersectionll1.add(1)
testIntersectionll1.add(1)
testIntersectionll1.add(3)
testIntersectionll1.add(2)
testIntersectionll1.add(6)
testIntersectionll2.add(2)
testIntersectionll2.add(2)
testIntersectionll2.add(3)
testIntersectionll2.add(2)
testIntersectionll2.add(6)
print(testIntersectionll1)
print(testIntersectionll2)
print(checkIntersection(testIntersectionll1, testIntersectionll2))
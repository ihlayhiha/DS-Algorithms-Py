class Node(object):

    def __init__(self, data) -> None:
        self.data = data
        self.nextnode = None

    def remove(self, data, previousNode):
        if self.data == data:
            previousNode.nextNode = self.nextnode
            del self.data
            del self.nextnode
        else:
            if self.nextnode is not None:
                self.nextnode.remove(data, self)
            

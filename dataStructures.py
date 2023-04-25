from typing import Optional

class Node:

    def __init__(self, data, doublyLinked: bool = False) -> None:
        
        self.data = data
        self.next = None

        if doublyLinked:
            self.prev = None
    

    def __repr__(self) -> str:

        return "<Node {}>".format(self.data)

    def __eq__(self, __o: object) -> bool:
        '''Checks if the data of the two nodes is the same, makes no comment on the pointers of the node.'''

        return self.data == __o.data
        


class LinkedList:

    def __init__(self, nodes: Optional[list] = None, doublyLinked: bool = False) -> None:

        self.doublyLinked = doublyLinked

        if nodes is None or nodes == []:
            self.head = None
            return

        
        head = Node(data=nodes.pop(0), doublyLinked=doublyLinked)
        self.head = head

        currentNode = self.head

        for i in range(len(nodes)):

            currentNode.next = Node(data=nodes[i], doublyLinked=doublyLinked)
            nextNode = currentNode.next

            if doublyLinked:
                nextNode.prev = currentNode
            
            currentNode = nextNode

    def __iter__(self):

        currentNode = self.head

        while currentNode is not None:
            yield currentNode
            currentNode = currentNode.next

    def __len__(self) -> int: 

        len = 0

        for _ in self:
            len += 1
        
        return len

    
    def __str__(self) -> str:

        if self.head is None:
            return "<LinkedList None>"

        linking = " <-> " if self.doublyLinked else " -> "
        strRep = "<LinkedList None <- " if self.doublyLinked else "<LinkedList "
        strRep += linking.join([str(node.data) for node in self]) + " -> None>"

        return strRep



    def __eq__(self, __o: object) -> bool:
        
        if self.doublyLinked != __o.doublyLinked:
            return False

        if len(self) != len(__o):
            return False

        selfNodes = [node for node in self]
        otherNodes = [node for node in __o]

        if self.doublyLinked:

            for i in range(len(selfNodes)):
                if selfNodes[i] != otherNodes[i] or selfNodes[i].next != otherNodes[i].next or selfNodes[i].prev != otherNodes[i].prev:
                    return False
            return True


        for i in range(len(selfNodes)):

                if selfNodes[i] != otherNodes[i] or selfNodes[i].next != otherNodes[i].next:
                    return False
            
        return True

    def addFirst(self, node: Node):

        node.next = self.head

        if self.doublyLinked: 
            node.prev = None
            if self.head is not None:
                self.head.prev = node
        
        
        self.head = node
    
    
    def addLast(self, node: Node):

        if self.head is None:
            self.head = node
            
            if self.doublyLinked:
                self.head.prev = None
            
            return
        
        for currentNode in self: 
            continue

        currentNode.next = node

        if self.doublyLinked:
            currentNode.next.prev = currentNode

        

class Stack: 

    def __init__(self, elements) -> None:
        pass
        


class TwoSum: 
    def __init__(self, elements: Optional[list[int]]) -> None:
        
        self.elements = elements
    
    def useLoop(self, target: int) -> Optional[list[int]]:

        for i in range(len(self.elements)): 
            for j in range(len(self.elements)):
                if self.elements[i] + self.elements[j] == target:
                    return [i,j]

        return None

    def useHashMap(self, target: int) -> Optional[list[int]]:

        elemsDict = {}

        for i in range(len(self.elements)):

            if target-self.elements[i] in elemsDict:
                return [i, elemsDict[target-self.elements[i]]]
            
            elemsDict[self.elements[i]] = i
        
        return None

        



def main():
    pass
    




if __name__ == "__main__":
    main()
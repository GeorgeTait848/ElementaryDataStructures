from typing import Optional


class StackUnderFlow(Exception):
    pass

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

        
        head = Node(data=nodes[0], doublyLinked=doublyLinked)
        self.head = head

        currentNode = self.head

        for i in range(1,len(nodes)):

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

        return 


    def pop(self):

        if self.head is None:
            return

        oldHead = self.head 
        self.head = self.head.next

        if self.doublyLinked and self.head is not None:
            self.head.prev = None

        return oldHead

    def reverse(self):

        currentNode = self.head
        prevNode = None

        while currentNode is not None:

            nextNode = currentNode.next
            currentNode.next = prevNode

            if self.doublyLinked:
                currentNode.prev = nextNode

            prevNode = currentNode
            currentNode = nextNode

        
        self.head = prevNode

        

class Stack: 

    def __init__(self, elements: Optional[list] = None):
        '''Implemlents a Stack from a list of elements, via a reversed linked list. Note, top is zero indexed, sp self.top = -1 refers to an empty stack'''

        if elements is None:
            self.top = -1
            self.elements = LinkedList()
            return

        self.top = len(elements) - 1
        self.elements = LinkedList(elements)
        self.elements.reverse()

    def __eq__(self, __o: object) -> bool:
        
        return self.elements == __o.elements

    def isEmpty(self):
        return self.top == -1

    def pop(self):

        if self.isEmpty():
            raise StackUnderFlow()
        
        self.top -= 1
        return self.elements.pop()

    def push(self, element: Node):

        self.top +=1
        self.elements.addFirst(node=element)

class Queue: 
    def __init__(self) -> None:
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

        

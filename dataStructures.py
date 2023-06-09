from typing import Optional


class StackUnderFlow(Exception):
    pass

class QueueUnderflow(Exception):
    pass

class QueueOverflow(Exception):
    pass

class ImproperKeysForBinaryTree(Exception):
    pass

class LinkedListNode:

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

        
        head = LinkedListNode(data=nodes[0], doublyLinked=doublyLinked)
        self.head = head

        currentNode = self.head

        for i in range(1,len(nodes)):

            currentNode.next = LinkedListNode(data=nodes[i], doublyLinked=doublyLinked)
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

    def addFirst(self, node: LinkedListNode):
        
        node.next = self.head

        if self.doublyLinked: 
            node.prev = None
            if self.head is not None:
                self.head.prev = node
        
        
        self.head = node
    
    
    def addLast(self, node: LinkedListNode):

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
        '''Implemlents a Stack from a list of elements, via a dictionary. The final element in elements is the top of the stack. Note, top is zero indexed, sp self.top = -1 refers to an empty stack. We are not yet 
        considering stack overflows.'''

        if elements is None:
            self.top = -1
            self.elements = {}
            return

        self.top = len(elements) - 1
        self.elements = {}

        for i in range(len(elements)):
            self.elements[i] = elements[i]

    def __getitem__(self, index):
            return self.elements[index]
        
    def __setitem__(self, index, item):
            self.elements[index] = item


    def __eq__(self, __o: object) -> bool:
        
        return self.elements == __o.elements

    def isEmpty(self):
        return self.top == -1

    def pop(self):

        if self.isEmpty():
            raise StackUnderFlow()
        
        self.top -= 1
        return self.elements.pop(self.top + 1)

    def push(self, element):

        self.top +=1
        self[self.top] = element

class Queue: 
    '''Represents a Queue data structure with zero indexed head and tail, implemented using dictionaries.'''

    def __init__(self, elements: Optional[list] = None, maxLength: int = 1e6):

        if elements is None: 
            self.head, self.tail = 0,0
            self.elements = {}
            self.maxLength = maxLength
            return
        
        if len(elements) > maxLength: 
            raise QueueOverflow()

        self.elements = {}
        self.head = 0
        self.maxLength = maxLength
        self.tail = len(elements) if len(elements) < maxLength else -1
        
        for i in range(len(elements)):
            self.elements[i] = elements[i]

    def __eq__(self, __o: object) -> bool:
        return self.head == __o.head and self.tail == __o.tail and self.elements == __o.elements

    
    def __getitem__(self, index: int):
        return self.elements[index]
    
    def __setitem__(self, index: int, item): 
        self.elements[index] = item

    def __contains__(self, item): 
        return item in self.elements
        

    def enqueue(self, item): 

        if self.head == self.tail + 1:
            raise QueueOverflow()

        if self.tail == -1: 
            self.tail = 0

        self[self.tail] = item
        
        if self.tail == self.maxLength:
            if self.head == 0:
                self.tail = -1
                return

        self.tail +=1

    def dequeue(self): 
        if self.head == self.tail:
            raise QueueUnderflow()
        
        val = self.elements.pop(self.head)
        prevHead = self.head

        if self.head == self.maxLength:
            self.head = 0
            return
        
        self.head +=1

        return {prevHead: val}

class BinaryTreeNode: 

    def __init__(self, key: Optional[any] = None) -> None:

        self.key = key
        self.left = None
        self.right = None
        self.parent = None

    def __eq__(self, __o: object) -> bool:
        return self.key == __o.key
    
    def addLeft(self, data):
        self.left = BinaryTreeNode(data)

    def addRight(self, data): 
        self.right = BinaryTreeNode(data)

    def __str__(self) -> str:
        return '<BinaryTreeNode key: {}>'.format(self.key)


class BinaryTree: 

    def __init__(self, nodes: Optional[dict] = None):

        if nodes is None:
            self.root = None
            return 
        
        self.root = self._initHelper(nodes)

    
    def _initHelper(self, nodes: dict): 

        if 'left' not in nodes and 'right' not in nodes:
            return BinaryTreeNode(nodes['key'])

        if 'left' in nodes and 'right' not in nodes:

            newNode = BinaryTreeNode(nodes['key'])
            newNode.left = self._initHelper(nodes['left'])
            newNode.left.parent = newNode
            return newNode
        
        if 'left' not in nodes and 'right' in nodes:

            newNode = BinaryTreeNode(nodes['key'])
            newNode.right = self._initHelper(nodes['right'])
            newNode.right.parent = newNode
            return newNode
        

        newNode = BinaryTreeNode(nodes['key'])
        newNode.right = self._initHelper(nodes['right'])
        newNode.right.parent = newNode

        newNode.left = self._initHelper(nodes['left'])
        newNode.left.parent = newNode

        return newNode

    def __str__(self) -> str:
        return self._strHelper(self.root)

    def _strHelper(self, node: BinaryTreeNode) -> str:
        
        if node is None: 
            return str(None)
        
        if node.left is None and node.right is None: 
            return str(node.key)
        
        if node.left is not None and node.right is None: 
            return "{}, {}".format(node.key, self._strHelper(node.left))
        
        if node.left is None and node.right is not None: 
            return "{}, {}".format(node.key, self._strHelper(node.right))
        
        return "{}, {}, {}".format(node.key, self._strHelper(node.left), self._strHelper(node.right))
            
        


class TwoSum: 
    def __init__(self, elements: Optional[list[int]] = None) -> None:
        
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

        
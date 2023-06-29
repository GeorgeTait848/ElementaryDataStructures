from dataStructures import Node, LinkedList, Stack, Queue
from dataStructures import StackUnderFlow, QueueOverflow, QueueUnderflow
import unittest


class LinkedListTests(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:

        super().__init__(methodName)

        self.testLinkedLists = [
            LinkedList(),
            LinkedList([1,2,3]),
            LinkedList([4,2,3,5,7]), 
            LinkedList([0]), 
            LinkedList(["a", "b", 1, "guy"]), 
            LinkedList(nodes=None, doublyLinked=True),
            LinkedList(nodes=[0,4,6], doublyLinked=True),
            LinkedList(nodes=[4,9,8,6,4], doublyLinked=True), 
            LinkedList(nodes=["cowboy"], doublyLinked=True), 
            LinkedList(nodes=["a", "b", 1, "guy"], doublyLinked=True), 
            LinkedList(nodes=["x", "xy", 1, 2, 3, 9, 5, 12, 0, 4], doublyLinked=True)
            ]

        
    def test_emptyLL(self): 

        emptyLL = LinkedList()
        self.assertEqual(emptyLL.head, None)

    def testDunderIter(self):

        nodesLists = [
            [], 
            [1,2,3], 
            [4,2,3,5,7], 
            [0], 
            ["a", "b", 1, "guy"], 
            [],
            [0,4,6], 
            [4,9,8,6,4],
            ["cowboy"], 
            ["a", "b", 1, "guy"], 
            ["x", "xy", 1, 2, 3, 9, 5, 12, 0, 4]
        ]

        for i in range(len(self.testLinkedLists)): 

            currentLL = self.testLinkedLists[i]
            currentNodesDataList = [node.data for node in  currentLL]

            self.assertEqual(currentNodesDataList, nodesLists[i])


    def testDunderLen(self): 

        testLengths = [0, 3, 5, 1, 4, 0, 3, 5, 1, 4, 10]

        for i in range(len(self.testLinkedLists)):
            self.assertEqual(len(self.testLinkedLists[i]), testLengths[i])


    
    def testDunderStr(self):

        singlyLLReps = [testLinkedList.__str__() for testLinkedList in self.testLinkedLists]

        correctLinkedListReps = [
            "<LinkedList None>",
            "<LinkedList 1 -> 2 -> 3 -> None>", 
            "<LinkedList 4 -> 2 -> 3 -> 5 -> 7 -> None>", 
            "<LinkedList 0 -> None>", 
            "<LinkedList a -> b -> 1 -> guy -> None>", 
            "<LinkedList None>",
            "<LinkedList None <- 0 <-> 4 <-> 6 -> None>", 
            "<LinkedList None <- 4 <-> 9 <-> 8 <-> 6 <-> 4 -> None>", 
            "<LinkedList None <- cowboy -> None>", 
            "<LinkedList None <- a <-> b <-> 1 <-> guy -> None>", 
            "<LinkedList None <- x <-> xy <-> 1 <-> 2 <-> 3 <-> 9 <-> 5 <-> 12 <-> 0 <-> 4 -> None>"
            ]

        for i in range(len(self.testLinkedLists)):
            self.assertEqual(singlyLLReps[i], correctLinkedListReps[i])

    
    def testDunderEq(self):

        others = [
            [
                LinkedList(), 
                LinkedList(nodes=None, doublyLinked=False), 
                LinkedList(nodes=None, doublyLinked=True), 
                LinkedList(nodes=[]), 
                LinkedList(nodes=[1,2])
            ],

            [
                LinkedList([1,2,3]), 
                LinkedList(nodes=[1,2,3], doublyLinked=False), 
                LinkedList(nodes=[1,2,3], doublyLinked=True), 
                LinkedList(nodes=[1,3,2]),
                LinkedList(nodes=[1], doublyLinked=True), 
                LinkedList(nodes=[1,2,3,0])
            ],

            [
                LinkedList([4,2,3,5,7]), 
                LinkedList(nodes=[4,2,3,5,7], doublyLinked=False),
                LinkedList(nodes=[4,2,3,5,7], doublyLinked=True), 
                LinkedList(nodes=[4,3,2,7,5])
            ], 

            [
                LinkedList([0]), 
                LinkedList([0], doublyLinked=False), 
                LinkedList([0], doublyLinked=True), 
                LinkedList([2]), 
                LinkedList([0,1])
            ],

            [
                LinkedList(["a", "b", 1, "guy"]),
                LinkedList(["a", "b", 1, "guy"], doublyLinked=True), 
                LinkedList(["ab", "1", "guy" ])
            ], 
            
            [
                LinkedList(nodes=None, doublyLinked=True),
                LinkedList(nodes=None, doublyLinked=False),
                LinkedList(nodes=[], doublyLinked=False), 
                LinkedList(nodes=[], doublyLinked=True)
            ],
            [
                LinkedList(nodes=[0,4,6], doublyLinked=True), 
                LinkedList(nodes=[0,4,6], doublyLinked=False),
                LinkedList(nodes=[0,4,6,[]], doublyLinked=True)
            ],
            [
                LinkedList(nodes=[4,9,8,6,4], doublyLinked=True), 
                LinkedList(nodes=[4,9,8,6,4], doublyLinked=False), 
            ], 

            [
                LinkedList(nodes=["cowboy"], doublyLinked=True), 
                LinkedList(nodes=["cowboy"], doublyLinked=False),
                LinkedList(nodes=["cowboys"], doublyLinked=True), 
                LinkedList(nodes=["c", "o", "w", "b", "o", "y"], doublyLinked=True)
            ], 

            [
                LinkedList(nodes=["a", "b", 1, "guy"], doublyLinked=True)
            ], 

            [
                LinkedList(nodes=["x", "xy", 1, 2, 3, 9, 5, 12, 0, 4], doublyLinked=True),
                LinkedList(nodes=["x", "xy", 1, 2, 3, 9, 5, 12, 0, 4], doublyLinked=False),
            ]

            ]

        othersEquiv = [
            [True, True, False, True, False], 
            [True, True, False, False, False, False], 
            [True, True, False, False], 
            [True, True, False, False, False], 
            [True, False, False],
            [True, False, False, True],
            [True, False, False], 
            [True, False], 
            [True, False, False, False],
            [True], 
            [True, False]

        ]

        for i in range(len(self.testLinkedLists)):
            for j in range(len(others[i])):
                self.assertEqual(self.testLinkedLists[i] == others[i][j], othersEquiv[i][j])


    def testAddFirst(self):

        nodes = [
            Node(0),
            Node("x"),
        ]

        correctListsAfterAdding = [
            [
                LinkedList(nodes=[0]), 
                LinkedList(nodes=["x", 0])
            ],

            [
                LinkedList([0,1,2,3]), 
                LinkedList(["x", 0,1,2,3])
            ],
            [
                LinkedList([0,4,2,3,5,7]),
                LinkedList(["x", 0,4,2,3,5,7]), 
            ],

            [
                LinkedList([0,0]),
                LinkedList(["x", 0, 0]), 
            ], 
            
            [
                LinkedList([0, "a", "b", 1, "guy"]),
                LinkedList(["x", 0, "a", "b", 1, "guy"])
            ], 

            [
                LinkedList(nodes=[0], doublyLinked=True), 
                LinkedList(nodes=["x", 0], doublyLinked=True)

            ],
            [
                LinkedList(nodes=[0,0,4,6], doublyLinked=True),
                LinkedList(nodes=["x", 0,0,4,6], doublyLinked=True) 
            ],
            
            [
                LinkedList(nodes=[0,4,9,8,6,4], doublyLinked=True),
                LinkedList(nodes=["x",0,4,9,8,6,4], doublyLinked=True), 
            ], 
            [
                LinkedList(nodes=[0, "cowboy"], doublyLinked=True),
                LinkedList(nodes=["x", 0, "cowboy"], doublyLinked=True)
            ], 

            [
                LinkedList(nodes=[0, "a", "b", 1, "guy"], doublyLinked=True),
                LinkedList(nodes=["x", 0, "a", "b", 1, "guy"], doublyLinked=True)
            ],

            [
                LinkedList(nodes=[0, "x", "xy", 1, 2, 3, 9, 5, 12, 0, 4], doublyLinked=True),
                LinkedList(nodes=["x", 0, "x", "xy", 1, 2, 3, 9, 5, 12, 0, 4], doublyLinked=True)
            ]
        ]



        for i in range(len(self.testLinkedLists)):
            currentLL = self.testLinkedLists[i]
            for j in range(len(nodes)):
                self.testLinkedLists[i].addFirst(nodes[j])
                self.assertEqual(self.testLinkedLists[i], correctListsAfterAdding[i][j])
            
            self.testLinkedLists[i] = currentLL
    

    def testAddLast(self): 

        addLastNode = Node(0)

        correctAddedLastNodeLists = [
            LinkedList([0]),
            LinkedList([1,2,3,0]),
            LinkedList([4,2,3,5,7,0]), 
            LinkedList([0,0]), 
            LinkedList(["a", "b", 1, "guy",0]), 
            LinkedList(nodes=[0], doublyLinked=True),
            LinkedList(nodes=[0,4,6,0], doublyLinked=True),
            LinkedList(nodes=[4,9,8,6,4,0], doublyLinked=True), 
            LinkedList(nodes=["cowboy",0], doublyLinked=True), 
            LinkedList(nodes=["a", "b", 1, "guy",0], doublyLinked=True), 
            LinkedList(nodes=["x", "xy", 1, 2, 3, 9, 5, 12, 0,4,0], doublyLinked=True)
            ]

        for i in range(len(self.testLinkedLists)):

            currentLL = self.testLinkedLists[i]

            self.testLinkedLists[i].addLast(addLastNode)
            self.assertEqual(correctAddedLastNodeLists[i], self.testLinkedLists[i])

            self.testLinkedLists[i] = currentLL

    def testPop(self): 

        correctPoppedLists = [
            LinkedList(), 
            LinkedList([2,3]), 
            LinkedList([2,3,5,7]), 
            LinkedList([]),
            LinkedList(['b', 1, "guy"]), 
            LinkedList(nodes=None, doublyLinked=True), 
            LinkedList(nodes=[4,6], doublyLinked=True),
            LinkedList(nodes=[9,8,6,4], doublyLinked=True), 
            LinkedList(nodes=[], doublyLinked=True), 
            LinkedList(nodes=["b", 1, "guy"], doublyLinked=True), 
            LinkedList(nodes=["xy", 1, 2, 3, 9, 5, 12, 0, 4], doublyLinked=True)
        ]

        for i in range(len(self.testLinkedLists)):

            currentLL = self.testLinkedLists[i]
            self.testLinkedLists[i].pop()

            self.assertEqual(correctPoppedLists[i], self.testLinkedLists[i])

            self.testLinkedLists[i] = currentLL

    
    def testReverse(self):

        correctReversedLists = [
            LinkedList(),
            LinkedList([3,2,1]),
            LinkedList([7,5,3,2,4]),
            LinkedList([0]),
            LinkedList(["guy", 1, "b", "a"]), 
            LinkedList(nodes=None, doublyLinked=True),
            LinkedList(nodes=[6,4,0], doublyLinked=True), 
            LinkedList(nodes=[4,6,8,9,4], doublyLinked=True), 
            LinkedList(nodes=["cowboy"], doublyLinked=True), 
            LinkedList(nodes=["guy", 1, "b", "a"], doublyLinked=True),  
            LinkedList(nodes=[4, 0, 12, 5, 9, 3, 2, 1, "xy", "x"], doublyLinked=True)
            ]

        for i in range(len(self.testLinkedLists)):
        
            currentLL = self.testLinkedLists[i]
            self.testLinkedLists[i].reverse()
            
            self.assertEqual(correctReversedLists[i], self.testLinkedLists[i])
            self.testLinkedLists[i] = currentLL

class StackTests(unittest.TestCase):

    def __init__(self, methodName: str = ...) -> None:

        super().__init__(methodName)
        self.testStacks = [
            Stack(), 
            Stack([1,2,3]), 
            Stack(["a", "b", 1, 4, 6]), 
            Stack([0 for _ in range(10)]), 
            Stack([])
        ]

    def testDunderEq(self):

        others = [
            [
                Stack(),
                Stack([]), 
                Stack([1])
            ], 
            [
                Stack([1,2,3]), 
                Stack([1,2,4]), 
                Stack([3,2,1]), 
                Stack([1,2])
            ], 
            [
                Stack(["a", "b", 1, 4, 6]), 
                Stack(["a", "b", 1, 6]), 
                Stack([6, 4, 1, "b", "a"]), 
                Stack(["a", "c", 1, 4, 6]), 
            ],

            [
                Stack([0 for _ in range(10)]), 
                Stack([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
                Stack([1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
                Stack([0, 0, 0, 0, 0, 0, 0, 0, 0])
            ], 

            [
                Stack([]), 
                Stack(), 
                Stack([1])
            ],

            ]

        othersEquiv = [
            [True, True, False], 
            [True, False, False, False],
            [True, False, False, False],
            [True, True, False, False],
            [True, True, False]
            ]

        for i in range(len(self.testStacks)):
            for j in range(len(others[i])):
                self.assertEqual(self.testStacks[i] == others[i][j], othersEquiv[i][j])

    
    def testIsEmpty(self): 

        empty = [True, False, False, False, True]

        for i in range(len(self.testStacks)):
            self.assertEqual(empty[i], self.testStacks[i].isEmpty())

    def test_push_pop(self):
        stack = Stack()
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.isEmpty())

    def test_stack_with_initial_elements(self):
        elements = [40, 50, 60]
        stack = Stack(elements)
        self.assertFalse(stack.isEmpty())
        for i, element in enumerate(elements):
            self.assertEqual(stack[i], element)
        self.assertEqual(len(stack.elements), len(elements))

    def test_setitem_getitem(self):
        stack = Stack([70, 80, 90])
        stack[1] = 85
        self.assertEqual(stack[1], 85)

    def test_equality(self):
        stack1 = Stack([100, 200, 300])
        stack2 = Stack([100, 200, 300])
        stack3 = Stack([400, 500, 600])
        self.assertEqual(stack1, stack2)
        self.assertNotEqual(stack1, stack3)

    def test_pop_empty_stack(self):
        stack = Stack()
        with self.assertRaises(StackUnderFlow):
            stack.pop()


class QueueTests(unittest.TestCase):

    def test_empty_queue(self):
        queue = Queue()
        self.assertEqual(queue.head, 0)
        self.assertEqual(queue.tail, 0)
        self.assertEqual(len(queue.elements), 0)
    
    def test_enqueue_dequeue(self):
        queue = Queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), {0: 1})
        self.assertEqual(queue.dequeue(), {1: 2})
        self.assertEqual(queue.dequeue(), {2: 3})
    
    def test_queue_with_initial_elements(self):
        elements = [4, 5, 6]
        queue = Queue(elements)
        self.assertEqual(queue.head, 0)
        self.assertEqual(queue.tail, len(elements))
        self.assertEqual(len(queue.elements), len(elements))
        for i, element in enumerate(elements):
            self.assertEqual(queue[i], element)

    def test_queue_overflow_init(self):
        elements = [1, 2, 3]
        with self.assertRaises(QueueOverflow):
            _ = Queue(elements, maxLength=2)

    def test_enqueue_overflow(self): 
        queue = Queue([1,2,3,4], maxLength=4)
        with self.assertRaises(QueueOverflow): 
            queue.enqueue(5)

    def test_boundary_case(self): 
        queue = Queue([1,2,3,4], maxLength=4)
        _ = queue.dequeue()
        queue.enqueue(5)
        self.assertEqual(queue.elements, Queue([5,2,3,4]).elements)

        q2 = Queue([3,4,2,1], maxLength=4)
        q2.dequeue()
        q2.dequeue()
        q2.enqueue(9)
        self.assertEqual(q2.elements, {0:9, 2:2, 3:1})

            
        
    def test_queue_underflow(self):
        queue = Queue()
        with self.assertRaises(QueueUnderflow):
            queue.dequeue()
            

        



def main():
    unittest.main(verbosity=2)



if __name__ == "__main__":
    main()




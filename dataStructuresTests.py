from dataStructures import Node, LinkedList, Stack, Queue
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



            

        



def main():
    unittest.main(verbosity=2)



if __name__ == "__main__":
    main()



class QueueTests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)

        self.testQueues = [
            Queue(),
            Queue([]), 
            Queue([1]), 
            Queue(["a", "b", "c", "d"]), 
            Queue([1, "xyz", 2, "a", "b"])
        ]

    def testDunderEq(self):

        others = [
            [
                Queue(), 
                Queue([]), 
                Queue(None), 
                Queue([0])
            ], 
            [
                Queue([]), 
                Queue(), 
                Queue(None), 
                Queue([2])], 
            [
                Queue([1]), 
                Queue([]), 
                Queue([0]), 
                Queue([1,2])
            ], 
            [
                Queue(["a", "b", "c", "d"]), 
                Queue(["a", "b", "c"]), 
                Queue(["a", "b", "c", "d", "d"]), 
            ], 
            [
                Queue([1, "xyz", 2, "a", "b"]), 
                Queue([1, "xyz", 2, "a"]), 
                Queue([1, "xyz", 2, "a", "b", "b"]), 
                Queue(["xyz", 2, "a", "b"])
            ]
        ]

        othersEquiv = [
                [True, True, True, False]
                [True, True, True, False], 
                [True, False, False, False],
                [True, False, False], 
                [True, False, False]   
            ]

        for i in range(len(self.testQueues)):
            for j in range(len(others[i])):
                self.assertEqual(self.testQueues[i] == others[i][j], othersEquiv[i][j])

        
        
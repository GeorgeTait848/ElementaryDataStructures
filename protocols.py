from typing import Protocol

class TreeTraversable(Protocol): 

    def preOrder(self):
        ...

    def inOrder(self): 
        ...

    def postOrder(self): 
        ...


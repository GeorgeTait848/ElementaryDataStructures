from typing import *

class ListNode:
    def __init__(self, val = None, next = None):
        pass

class LinkedListProblems: 
    def __init__(self) -> None:
        pass

    def twentyOne_mergeSortedLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dum = ListNode()
        curr = dum

        while list1 and list2: 

            if list1.val < list2.val: 
                curr.next = list1
                curr = list1
                list1 = list1.next
                continue

            curr.next = list2
            curr = list2
            list2 = list2.next
        
        curr.next = list1 if list1 else list2

        return dum.next

    def eightyThree_deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        while curr and curr.next: 
            if curr.val == curr.next.val:
                curr.next = curr.next.next
                continue
            curr = curr.next

        return head

    def TwoHundredThree_removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        #Solution uses two pointers, the previous pointer (prev) points to the last visited node, and curr refers to the current node. 
        #if the current node's value equals the target value to remove, we act as if we never visited that node. 
        dum = ListNode(next=head)
        prev, curr = dum, head

        while curr:

            if curr.val == val: 
                prev.next = curr.next
            else:
                prev = curr

            curr = curr.next

        return dum.next 


    def TwoHundredSix_reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #three pointers, one to store the previous node (used to update the next pointer of the current node)
        #one to store the next node, which is used to move to the next iteration
        #the current node to perform the operations on. 
        
        prev, curr, nxt = None, head, None

        while curr: 
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
def main():
    
    temp = {}
    temp[0] = None

    print(True) if None in temp else print(False)
    



if __name__ == "__main__":
    main()
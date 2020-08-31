# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a new list node with a value of 0
        new_node = ListNode(0)
        
        # Check if either list exists
        if not l1:
            return l2
        if not l2:
            return l1
        
        # If the value of l1 is < the value of l2
        # We need to start with l1
        if l1.val < l2.val:
            # Set the new node's next to l1
            new_node.next = l1
            # Go to the next node in l1 and recurse
            new_node.next.next = self.mergeTwoLists(l1.next, l2)
        # Otherwise, list 2 is shorter so we need to go here next
        else:
            # Set the new node's next to l2
            new_node.next = l2
            # Go to the next node in l2 and recurse
            new_node.next.next = self.mergeTwoLists(l1, l2.next)
            
        return new_node.next

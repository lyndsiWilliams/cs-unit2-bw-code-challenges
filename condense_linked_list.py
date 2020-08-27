# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def condense_linked_list(node):
    # Reference the current node's value
    current = node
    
    # List to store the values
    condensed_list = []
    
    # Loop through the list
    while current:
        # If the current value is already in the list
        if current.value in condensed_list:
            # Delete it
            current.value = None
        # Otherwise, append the current value to the list
        else:
            condensed_list.append(current.value)
        # Move to the next node
        current = current.next
        
    return condensed_list

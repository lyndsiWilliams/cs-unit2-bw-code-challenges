class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Contains items as they are added
        self.stack = []
        # Used to reverse the order of the stack
        # during the pop operation
        self.reversed = []
        # Top of stack is recorded for O(1) peek
        self.top = None
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        # If the stack doesn't exist yet
        if not self.stack:
            # Assign parameter x as top
            self.top = x
            # Append the value to the stack
            self.stack.append(x)
        else:
            # Otherwise, this is a pre-existing stack so
            # append the value to the stack as normal
            self.stack.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        # If the element isn't being popped from the reversed stack
        if not self.reversed:
            # Loop through the current stack
            while self.stack:
                # Append the elements in reversed order to the reversed stack (flip it)
                # then pop the last value
                self.reversed.append(self.stack.pop())
        # Otherwise the element IS being popped from the reversed stack, so
        # pop the element normally
        return self.reversed.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        # If the element is inside the reversed stack
        if self.reversed:
            # Return the last item from the reversed stack
            return self.reversed[-1]
        # Otherwise, return the stored top element
        return self.top
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        # This will return True if stack and reversed are empty
        return not self.stack and not self.reversed
        


# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())
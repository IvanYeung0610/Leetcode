"""
Ivan Yeung

155. Min Stack
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

    MinStack() initializes the stack object.
    void push(int value) pushes the element value onto the stack.
    void pop() removes the element on the top of the stack.
    int top() gets the top element of the stack.
    int getMin() retrieves the minimum element in the stack.

You must implement a solution with O(1) time complexity for each function.
"""

class MinStack:

    def __init__(self):
        self.stack: list[int] = []
        self.min_stack: list[int] = []

    def push(self, value: int) -> None:
        self.stack.append(value)
        if len(self.min_stack) == 0 or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self) -> None:
        popped_val = self.stack.pop()
        if popped_val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

    # This solution uses two stacks. An alternative is using one stack
    # where we store the value being pushed along with the current min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

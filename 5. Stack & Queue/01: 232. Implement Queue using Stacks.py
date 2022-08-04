”https://leetcode.com/problems/implement-queue-using-stacks/“
  
# Stack => Queue
# FILO  => FIFO
# Using two stacks: stack_in & stack_out
# 讲得好！ https://www.youtube.com/watch?v=RzT6YgrGTyg

class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        
    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        # Get the correct order
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        # Get the element to be popped
        ans = self.stack_out.pop()
        # Add back
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())
        return ans

    def peek(self) -> int:
        # Get the correct order
        while self.stack_in:
            self.stack_out.append(self.stack_in.pop())
        # Get the top element
        ans = self.stack_out[-1]
        # Add back
        while self.stack_out:
            self.stack_in.append(self.stack_out.pop())
        return ans

    def empty(self) -> bool:
        # 同时为空
        return not self.stack_in and not self.stack_out
        

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

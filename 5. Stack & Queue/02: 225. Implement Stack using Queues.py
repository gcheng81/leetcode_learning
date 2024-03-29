"https://leetcode.com/problems/implement-stack-using-queues/"

# Queue => Stack
# Solution 1: Using only one queue
# Reference: https://www.youtube.com/watch?v=rW4vm0-DLYc
class MyStack:

    def __init__(self):
        self.queue = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.popleft())
        return self.queue.popleft()
        

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue
        #return len(self.queue)==0
        


# Solution 2: Using two queues
class MyStack:

    def __init__(self):
        self.queue = deque()
        self.tmp = deque()
        
    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        if self.empty():
            return None
        
        for _ in range(len(self.queue) - 1):
            self.tmp.append(self.queue.popleft())
        self.tmp, self.queue = self.queue, self.tmp
        return self.tmp.popleft()
        

    def top(self) -> int:
        if self.empty():
            return None
        return self.queue[-1]

    def empty(self) -> bool:
        return not self.queue
        #return len(self.queue)==0
        

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

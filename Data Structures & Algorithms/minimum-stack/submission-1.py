class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None
        

    def push(self, val: int) -> None:
        if val is not None: 
            self.stack.append(val)
            if self.min is None or (self.min is not None and val < self.min): 
                self.min = val
        return                  

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            if not self.stack:
                self.min = None
            elif val == self.min: 
                self.min = min(self.stack)
            
        
    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        return self.min



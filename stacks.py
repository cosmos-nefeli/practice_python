class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):

#Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

#use peek to look at the top of the stack

    def peek(self):
        return self.stack[-1]

# Use elist method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the stack")
        else:
            return self.stack.pop()


aStack = Stack()
aStack.add("Mon")
aStack.add("Tue")
aStack.add("Wed")
print(aStack.stack)
print("#Remove the top most element")
print(aStack.remove())
# Author: Anish Talluri
# Date: March 8th 2023
# File Goal: Creates a Stack class to store things in

class Stack:
    
    def __init__(self):
        self.lst = [] 

    def isEmpty(self):
        return self.lst == []

    def push(self, item):
        self.lst.append(item)

    def pop(self):
        return self.lst.pop()
    
    def peek(self):
        if len(self.lst) == 0:
            return None
        return self.lst[len(self.lst) - 1]

    def size(self):
        return len(self.lst)

# a driver program for class Stack

if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None

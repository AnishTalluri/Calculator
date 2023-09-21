# Author: Anish Talluri
# Date: March 8th 2023
# File Goal: Creates a functioning calculator (referencing stack class and expression tree) by referencing the operators and operands and performing a mathematical function

from stack import Stack
import tree

def infix_to_postfix(infix):
    postfix = []
    opStack = Stack()
    ops = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3, '^': 4}
    tokens = list(infix)
    n = []
    for i in tokens:
        if i in '0123456789.':
            n.append(i)
        else:
            if len(n) > 0:
                postfix.append(''.join(n))
                n.clear()
        if i == '(':
            opStack.push(i)
        if i == ')':
            while opStack.isEmpty() != True and opStack.peek() != '(':
                postfix.append(opStack.pop())
            opStack.pop()
        if i in '+-/*^':
            while(opStack.isEmpty() == False and ops[opStack.peek()] > ops[i]):
                postfix.append(opStack.pop())
            opStack.push(i)
    if len(n) > 0:
        postfix.append(''.join(n))
        n.clear()
    while opStack.isEmpty() == False:
        postfix.append(opStack.pop())
    joined = ' '.join(postfix)
    return joined

def calculate(infix):
    postfix = infix_to_postfix(infix)
    t = tree.ExpTree.make_tree(postfix.split())
    return tree.ExpTree.evaluate(t)


# a driver to test calculate module
if __name__ == '__main__':

    # test infix_to_postfix function
    assert infix_to_postfix('(5+2)*3') == '5 2 + 3 *'
    assert infix_to_postfix('5+2*3') == '5 2 3 * +'

    # test calculate function
    assert calculate('(5+2)*3') == 21.0
    assert calculate('5+2*3') == 11.0

    print("Welcome to Calculator Program!")
    while True:
        x = input("Please enter your expression here. To quit enter 'quit' or 'q': ")
        if x == "q" or x == "quit":
            print("Goodbye!")
            break
        try:
            print(calculate(x))
        except:
            print("Error: Invalid expression")

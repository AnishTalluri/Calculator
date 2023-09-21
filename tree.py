# Author: Anish Talluri
# Date: March 8th 2023
# File Goal: Creates a Binary Tree + Expression Tree using operators as the roots and numbers as the nodes

from stack import Stack

class BinaryTree:
    def __init__(self,rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s

class ExpTree(BinaryTree):
    
    def make_tree(postfix): # Create the Expression Tree
        stack = Stack()
        for i in postfix:
            if i == '.' or i.isdigit():
                stack.push(BinaryTree(i))
            else:
                temp = BinaryTree(i)
                temp.insertRight(stack.pop())
                temp.insertLeft(stack.pop())
                stack.push(temp)
        return ExpTree(stack.pop())
    
    def preorder(tree): # Traverses the ExpTree to get the prefix order of the tree
        if tree.getRootVal().getLeftChild() == None:
            if tree.getRootVal().getRightChild() == None:
                return tree.getRootVal().getRootVal()
        else:
            s = tree.getRootVal().getRootVal() + ExpTree.preorder(tree.getRootVal().getLeftChild()) + ExpTree.preorder(tree.getRootVal().getRightChild())
            return s

    def inorder(tree): # Traverses the ExpTree to get the nodes in non-decreasing order
        if tree.getRootVal().getLeftChild() == None:
            if tree.getRootVal().getRightChild() == None:
                return tree.getRootVal().getRootVal()
        else:
            s = "(" + ExpTree.inorder(tree.getRootVal().getLeftChild()) + tree.getRootVal().getRootVal() + ExpTree.inorder(tree.getRootVal().getRightChild()) + ")"
            return s
      
    def postorder(tree): # Traverses the ExpTree to get the postfix order of the tree
        if tree.getRootVal().getLeftChild() == None:
            if tree.getRootVal().getRightChild() == None:
                return tree.getRootVal().getRootVal()
        else:
            s = ExpTree.postorder(tree.getRootVal().getLeftChild()) + ExpTree.postorder(tree.getRootVal().getRightChild()) + tree.getRootVal().getRootVal()
            return s

    def evaluate(tree): # Evaluates the ExpTree and returns the result of the left and right sums of the tree (based on the operator of course)
        if tree.getRootVal().getRootVal() == None:
            return None
        if tree.getRootVal().getLeftChild() == None:
            if tree.getRootVal().getRightChild() == None:
                return tree.getRootVal().getRootVal()

        l_sum = float(ExpTree.evaluate(tree.getRootVal().getLeftChild()))
        r_sum = float(ExpTree.evaluate(tree.getRootVal().getRightChild()))

        if tree.getRootVal().getRootVal() == '+':
            return l_sum + r_sum

        elif tree.getRootVal().getRootVal() == '-':
            return l_sum - r_sum

        elif tree.getRootVal().getRootVal() == '*':
            return l_sum * r_sum

        else:
            return l_sum / r_sum

    def __str__(self):
        return ExpTree.inorder(self)
   
# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':

    # test a BinaryTree
    
    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild()== None
    assert r.getRightChild()== None
    assert str(r) == 'a()()'
    
    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'
    
    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'
    
    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    
    # test an ExpTree
    
    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    print("Hello")

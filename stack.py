# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:09:25 2016
STACK
[1][2][3][4][][]
|           | ^--- oben (Letzte moegliche Position)
|           |
|           ^--- StackPointer (Zeigt auf erste freie Position)
|
^---Unten (Erstes Moegliche Position)  

"""
from node import *

class Stack(object):
    def __init__(self,n):
        self.stack  = LinkedList(None) # Create a new Node obj.
        self.lower = 0                 # 
        self.upper = n                 # Stack is limited
        self.sp    = 0
    def isFull(self):
        """ Return true if stack is full 
        """
        return self.sp > self.upper
    def isEmpty(self):
        """ Returns true if stack is empty
        """
        # Check if HEAD is type None - empty
        return self.stack.pointer.value is None 

    def push(self, element):
        """ Push values on the stack
        """
        if self.isFull():
            print("Stack is full")
        else:
            self.stack.pre(element)
            self.sp = self.sp + 1
    def pop(self):
        """ Poppen
        """
        if self.isEmpty:
            return None
        else:
            self.stack.rm(self.stack.pointer.value)
            self.sp = self.sp - 1
    def top(self):
        """ Top Value
        """
        return self.stack.pointer.value
    def popTop(self):
        """ Poppen and top value
        """
        tVar = self.top()
        self.pop()
        return tVar







#class Stack(object):
#    def __init__(self,n):
#        """ Initialize Stack
#        Fill the stack with nonetypes
#        """
#        self.sp    = 0
#        self.unten = 0
#        self.oben  = n-1
#        self.stack = Node(None)
#        
#        # Verkettete Liste...
#        for i in range(self.oben):
#            self.stack.append(None)
#                
#        
#        #self.stack = [None]*n
#        
#    def isFull(self):
#        """ Return true if stack is full
#        """
#        return self.sp > self.oben
#        
#    def isEmpty(self):
#        """ Return true if stack is empty 
#        """
#        # If sp is lower or eq. unten return true
#        return self.sp <= self.unten
#    def push(self, element): 
#        """ Push a new element on the stack
#        """
#        # Stack full??
#        if(self.isFull()):
#            return False
#        else:
#            self.stack.append(element)
#            #self.stack[self.sp] = element
#            self.sp = self.sp + 1
#    def pop(self):
#        """ Decreases stack-pointer only
#        """
#        if(self.isEmpty()):
#            return False
#        else:
#            self.sp = self.sp - 1
#            # Change type to none
#            #self.stack[self.sp] = None
#    def top(self):
#        """ Returns first top element
#        """
#        if(self.isEmpty()):
#            return None
#        else:
#            return self.stack[self.sp-1]
#    def popTop(self):
#        """ Returns and removes first top element
#        """
#        tVar = self.top()
#        self.pop()
#        return tVar
        

myStack = Stack(100)
myStack.push(10)
print(myStack.top())
iVar = myStack.popTop()
print(iVar)
iVar = myStack.popTop()
print(iVar)





















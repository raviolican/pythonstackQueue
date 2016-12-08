# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 23:00:40 2016
Sieb des Eratosthenes
@author: frye
"""
from stackqueue import *

class Sieb(object):
    def __init__(self, n):
        self.num = n

        self.iQueue = StackQueue(n+1)
        for i in range(2,n+1):
            self.iQueue.enqueue(i)
            
    def compute(self):
        # First Number
        div = self.iQueue.dequeue()
        print(div)
        #print(div)
        if div is None:
            return 
        x = 0
        for i in range(self.num):
            iVal = self.iQueue.dequeue()
            try:  
                if iVal % div is not 0:
                    self.iQueue.enqueue(iVal)
                # Drehe die obige Operation um und schau ob es eine kleinere Zahl
                # gibt. Damit diese Zahl entfernt word.
                elif((div%iVal)%iVal is not 0): 
                    self.iQueue.enqueue(div)
                    continue
                else:
                    #print(div)
                    continue
            except TypeError:
              continue #finished
        self.compute()
    

        
            
        
myV = Sieb(100)
myV.compute()
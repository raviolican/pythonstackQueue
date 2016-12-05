# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:47:36 2016
QUEUE:
(i) Noch 1 element möglich:
<-   -    -- - -- -  -    -  ->                                   
..A]|[B][C][D][E][F][G][H][]|[A..
|                         ^ End; Hier werden Objekte angehängt
|
^ Start; Das Objekt wird ausgegeben

Den Queue kann man als Kreis ansehen. Dabei bewegen sich Anfang und Ende
unabhängig voneinander - aber abhängig davon wie schnell Aufgaben entnommen bzw
eingefügt werden.
Der Queue ist voll, wenn das letzte Element belegt ist.
@author: frye
"""

class Queue(object):
    def __init__(self, n):
        self.start  = 0
        self.end    = 0
        self.maximum = n
        self.voll    = False
        self.queue   = [None]*n
    def isEmpty(self):
        """ Returns if queue is empty
        """
        return self.start == (self.end and not self.voll)
        
    def isFull(self):
        return self.voll
        
    def enqueue(self, element):
        if(self.isFull()):
            return "Queue is Full"
        else:
            self.queue[self.end] = element
            # Wenn end == max wird end 0 ansonsten wird es die Zahl
            self.end = (self.end + 1) % self.maximum
            if(self.start == self.end):
                
                self.voll = True
                
    def dequeue(self):
        """ Returns first element and increses start
        """
        if( self.isEmpty()):
            return None
        else:
            self.voll = False
            iVar = self.queue[self.start]
            self.start = (self.start + 1) % self.maximum
            return iVar
            
    def front(self):
        """ Return first element
        """
        if(self.isEmpty()):
            return None
        else:
            return self.queue[self.start]
            
myQueue = Queue(10)
myQueue.enqueue("10101")
sVar = myQueue.get()
print(sVar)

for i in range(10):
    myQueue.enqueue(i)
for i in range(10):
    print(str(i)+" ---> " + str(myQueue.get()))













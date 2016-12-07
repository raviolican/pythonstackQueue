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
from node import LinkedList

class Queue(object):
    def __init__(self, n):
        self.start  = 0
        self.end    = 0
        self.maximum = n
        self.voll    = False
        self.queue   = LinkedList(None)
    def isEmpty(self):
        """ Returns if queue is empty
        """
        #return self.start == (self.end and not self.voll)
        return self.queue.pointer.value is None
        
    def isFull(self):
        return self.voll
        
    def enqueue(self, element):
        if(self.isFull()):
            return "Queue is Full"
        else:
            self.queue.pre(element)
            #oldself.queue[self.end] = element
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
            iVar = self.queue.pointer.value
            self.queue.rm(iVar)
            #iVar = self.queue[self.start]
            self.start = (self.start + 1) % self.maximum
            return iVar
            
    def front(self):
        """ Return first element
        """
        if(self.isEmpty()):
            return None
        else:
            return self.queue.pointer.value
            
            
            
myQueue = Queue(10) # Stack fuer 10 Elemente anlegen

for i in range(12):
    myQueue.enqueue(i)
for i in range(12):
    print(str(i)+" ---> " + str(myQueue.dequeue()))













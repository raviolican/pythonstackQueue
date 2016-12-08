# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 19:42:15 2016
Aufgabe 7.2:Queue

@author: frye
"""

from stack import Stack


class StackQueue(object):
    def __init__(self, stackLength):
        self.stackLength = stackLength
        self.inbox  = Stack(self.stackLength)
        self.outbox = Stack(self.stackLength)
         
    def enqueue(self, element):
        """ Add a new element in the inbox
        """
        self.inbox.push(element)
        
    def dequeue(self):
        """ Take an element from the outhbox
        """
        tVar = self.outbox.popTop()
        # If outbox is empty, none will be retur
        if(tVar == None):
            # Load all objects from inbox into the outbox
            for i in range(self.stackLength):
                tVar = self.inbox.popTop()
                # Only call until inbox is empty!
                if(self.inbox.isEmpty() == True):
                    break
                else:
                    self.outbox.push(tVar)
        return tVar
    




# Complexität:
# Enqueue O(1) Weil nur eine Funktion aufgerufen wird
# Dequeue Maximal O(N)| n = anzahl der Elemente in der inbox










#
#### TESTS ###
#
#
## Neues Objekt anlegen
#myQueue = StackQueue(20)
#
## Queue bietet für 10 Daten platz
#for i in range(10):
#    myQueue.enqueue(i*i)
#
#
#
## genau 10 mal daten aus dem Stack entfernen
#tVar = myQueue.dequeue()
#print(tVar)
#tVar = myQueue.dequeue()
#print(tVar)
#tVar = myQueue.dequeue()
#print(tVar)
#tVar = myQueue.dequeue()
#print(tVar)
#tVar = myQueue.dequeue()
#print(tVar)
#tVar = myQueue.dequeue()
#print(tVar)
#tVar = myQueue.dequeue()
#print(tVar)
#tVar = myQueue.dequeue()
#print(tVar)
#tVar = myQueue.dequeue()
#print(tVar)
#tVar = myQueue.dequeue()
#print(tVar)
#
## Das sollte nichtmehr funktionieren
#tVar = myQueue.dequeue()
#print(tVar) # Ausgabe: none
#
#
## Überfuellen - Der queue sollte alles ab 10 ignorierein
#for i in range(20):
#    myQueue.enqueue(i*i/2)
#
#for i in range(11):
#    print(myQueue.dequeue())
#
#
#
#
#

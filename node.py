# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:53:51 2016
Einfach Verkettete Liste
"""

class DataObj(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList(object):
    def __init__(self,value):
        # " Zeiger " auf den ersten Listeneintrag
        self.pointer = DataObj(value)
        
    def pre(self,value):
        """ Prepend
        """
        newObject = DataObj(value)
        newObject.next = self.pointer
        self.pointer = newObject
        
    def add(self,value):
        """ Append
        """
        newObject = DataObj(value)
        t = self.pointer
        while t.next is not None:
            t = t.next
        t.next = newObject 
        
    def rm(self, value):
        """ Delete
        """
        t = self.pointer
        if self.pointer.value is value:
            self.pointer = self.pointer.next
        while (t.next is not None) and (t.next.value is not value):
            t = t.next
        if t.next is not None:
            t.next = t.next.next
       
#   OPTIONAL
#    def va(self):
#        """ Get
#        """
#        return self.pointer.value
#        
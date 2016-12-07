# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 17:53:51 2016
Einfach Verkettete Liste
"""

class Node:
    def __init__(self, d):
        self.data = d       #d ist erstes Element(Kopf der Liste)
        self.next = None    #nächstes Element None

def prepend(data, list):    
    node = Node(data)       # neues Element am Anfang der Liste
    node.next = list        # altes Element an 2ter Stelle
    return node

def append(data, list):     # Neues Element am Ende der Liste
    node = Node(data)
    if list is None:        
        node.next = None    
        return node
    i = list
    while i.next is not None:
        i = i.next          #i = counter, wenn mit List gearbeitet wird, geht Kopf der Liste verloren
    i.next = node
    node.next = None
    return list

def delete(data, list):     #löscht ein Element aus Liste
    if list is None:        #nix zum löschen
        return None         
    if list.data is data:   #wenn erstes Element = data ist, Kopf der Liste um 1 weiter"
        return list.next
    
    i = list
    while i.next is not None and i.next.data is not data:   #sucht den zu löschenden Wert
        i = i.next
    if i.next is not None:
        i.next = i.next.next        #zeigt auf "übernächsten wert", da "nächste" Wert der neue Wert ist.
    return list

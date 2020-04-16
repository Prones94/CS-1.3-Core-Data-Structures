# Basic Structure for Stack using Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head == None:
            return True
        else:
            return False
        
    def push(self, data):
        if not self.is_empty():
            self.head = Node(data)

        else:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
    def pop(self):
        if self.is_empty():
            return None
        else:
            poppedNode = self.head
            self.head = self.head.next
            poppedNode.next = None
            return poppedNode.data
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.head.data
        
    def display(self):
        iternode = self.head
        if self.is_empty():
            print('Nothing here')
        else:
            while(iternode != None):
                print()


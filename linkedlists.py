"""
    Python does not have linked lists in its standard library. We implement the concept of linked lists using the concept of nodes 
"""

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

#print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def atBegining(self,newdata):
        newNode = Node(newdata)

# update the new nodes next val to existing node
        newNode.nextval = self.headval
        self.headval = newNode

list1 = SLinkedList()
list1.headval = Node("Mon")
print(list1.headval.dataval)

e2 = Node("Tue")
e3 = Node("wed")

list1.headval.nextval = e2

e2.nextval = e3

list1.listprint()

list1.atBegining("Sun")

list1.listprint()
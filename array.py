from array import *

#declare and intilise
array1 = array('i', [10,20,30,40,50])

for x in array1:
    print(x)

#accessing array element
print("#accessing array element")
print("array1[0] :" + str(array1[0]))
print("array1[2] :" + str(array1[2]))

#insertion Operation
print("#insertion Operation at position 1")
array1.insert(1,60)

for x in array1:
    print(x)

#deletion operation
print("#deletion Operation of element 40")
array1.remove(40)

for x in array1:
    print(x)

#   Search Operation 
print("#Search operation ")
print(array1.index(60))
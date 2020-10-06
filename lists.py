# This module will designed to practice python

#List is a collection which is ordered and changable.Allows duplicate members.

#create a list
thislist =["apple","banana","cherry"]
#print the list
print(thislist)
#print first value
print(thislist[0])
#negative index, print last item
print(thislist[-1])
#specify the range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#By leaving start value
print(thislist[:4])
#by leaving last value
print(thislist[4:])
#by giving neagtive range
print(thislist[-4:-1])
#change item
thislist[1]="black current"
print(thislist)
#loop through the items
for i in thislist:
    print(i)

#check if item exists or not

if "cherry" in thislist:
    print("cherry exists")

if "banana" not in thislist:
    print("banana doesn't exists")

#check the length
print(len(thislist))

#add items from end
thislist.append("orange")
print(thislist)

#add data at particular index
thislist.insert(2,"orangeee")
print(thislist)

#remove particular element
thislist.remove("orangeee")

#remove element from end
thislist.pop()
print(thislist)

#delete the list
del thislist[0]
print(thislist)

#clear the elements of list
thislist.clear()
print(thislist)



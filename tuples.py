""" A tuple is a sequence of immutable Python object
    The differences between tuples and lists are, the tuples cannot be changed unlike lists and tuples use parentheses, 
    whereas lists use square brackets
"""

#empty tuple
tup1 = ()

#single value
tup1 = (5,)

#access tuple value
tup2 = (1,2,3,4,5,6)
print("tup2[0]: ", tup2[0])

#update of tuple is not allowed but you can create new tuple 
tup3 = tup2 + tup1
print(tup3)

#delete tuple elements
del tup1


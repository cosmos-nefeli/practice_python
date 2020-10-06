"""
    elements in the set cannot be duplicates
    elements in set are immutable(cannot be modified) but the set as a whole is mutable
    There is no index attached to any elements in a python set
"""

Days = set(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])
print("#adding data to set")
Days.add("Sun")
print(Days)

# removing item from a set
Days.discard("Sun")
print(Days)



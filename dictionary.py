"""
     Dictionary data types in python. Till python 3.5, dictionary was unordered data structure, after 3.9 
     Keys are always unique and immutable
"""

dict = {'Name': 'Snigdha', 'Class':'First'}
print(dict)

#  updating Dictionary
dict['Class'] = 'Top'
print(dict)

#delete dictionary elements
del dict['Name']
print(dict)

dict.clear()
print(dict)
"""
    Python Maps also called ChainMap is a type of data structure to manage multiple dictionaries together as one unit.
"""

import collections

dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

res =  collections.ChainMap(dict1, dict2)

# Creating a single dictionary
print(res.maps,'\n')

print('Keys = {}'.format(list(res.keys())))
print('Values = {}'.format(list(res.values())))
print()

# print all the elements from results
print('element')
for key, val in res.items():
    print('{} = {}'.format(key, val))
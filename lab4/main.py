import random
import numpy as np


test_arr = [
    [3, 2],
    [5, 3],
    [4, 6],
    [5, 6],
    [7, 7],
    [1, 2]
]


size = int(input('Enter rucksack size  '))
N = int(input('Enter number of generations  '))
items = []
print('Enter item size and value')
print('      size: value:')
result = input("test arr?")
if result == "":
    items = test_arr
while result != "":
    item = input('item: ')
    if item =="":
        break
    items.append([int(i) for i in item.split(' ')])

vec = [[ random.randint(0, 1) for i in range(0, len(items))] for i in range(0, 7)]


values = [ np.add.reduce( np.multiply(i , [ j[0] for j in items] )) for i in vec]
weights = [ np.add.reduce( np.multiply(i , [ j[1] for j in items] )) for i in vec]

data = zip(vec , zip(values, weights))
parents = filter(lambda x:  x[1][1] <= size, data)
print(list(parents))
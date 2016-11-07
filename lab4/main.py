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

s = 5

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

vec = [[ random.randint(0, 1) for i in range(0, len(items))] for i in range(0, 13)]


values = [ np.add.reduce( np.multiply(i , [ j[0] for j in items] )) for i in vec]
weights = [ np.add.reduce( np.multiply(i , [ j[1] for j in items] )) for i in vec]
data = zip(vec , zip(values, weights))
parents = list(filter(lambda x:  x[1][1] <= size, data))
values = list(map(lambda x: x[1][0], parents))
sigma = np.std(values)**0.5
f_avg = np.mean(values)
F = [ 1+( (f + f_avg)/2 * sigma)  for f in values]
F_sum = sum(F)
p =[ F_i / F_sum for F_i in F]
res = set()
while True:
    i = np.random.choice(range(len(list(parents))), p=p)
    res.add(parents[i])
    if len(res) == s:
        break

print(res)
    

#print(np.array(list(parents)))

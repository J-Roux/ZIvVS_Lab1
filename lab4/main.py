import random
import numpy as np
import itertools

test_arr = [
    [3, 2],
    [5, 3],
    [4, 6],
    [5, 6],
    [7, 7],
    [1, 2],
    [3, 5],
    [8, 4],
    [2, 2]
]


s = 5
size = 27
N = 5
gen_size = 15
print('s = %i' % s)
print('size = %i' % size)
print('gen_size = %i' % gen_size)
print('Number of generations = %i' % N)
print('Number of individual  = %i' % (gen_size * N))
items = []

items = test_arr

vec = [[ random.randint(0, 1) for i in range(0, len(items))] for i in range(0, gen_size)]
best = set()
def count_weight_and_value(vec, items):
    values = [ np.add.reduce( np.multiply(i , [ j[0] for j in items] )) for i in vec]
    weights = [ np.add.reduce( np.multiply(i , [ j[1] for j in items] )) for i in vec]
    return zip(vec , zip(values, weights))


def iteration(vec, items, best, generation_size, s, size):
    data = count_weight_and_value(vec, items)
    parents = list(filter(lambda x:  x[1][1] <= size, data))
    values = list(map(lambda x: x[1][0], parents))
    sigma = np.std(values)**0.5
    f_avg = np.mean(values)
    F = [ 1+( (f + f_avg)/2 * sigma)  for f in values]

    best.add((tuple(parents[np.argmax(F)][0]), parents[np.argmax(F)][1]))
    F_sum = sum(F)
    p =[ F_i / F_sum for F_i in F]
    res = set()

    while True:
        i = np.random.choice(range(len(list(parents))), p=p)
        parents[i] = ( tuple(parents[i][0]), parents[i][1])
        res.add(parents[i])
        if len(res) == s:
            break
    parents = [x for x in parents if not (tuple(x[0]), x[1]) in res]


    r = []
    for  i in res:
        r.append((i , parents[np.argmax([ np.linalg.norm(np.array(i[0]) - np.array(j[0])) for j in parents])]))
        del  parents[np.argmax([ np.linalg.norm(np.array(i[0]) - np.array(j[0])) for j in parents])]

    r = [[i1 if(i1 == i2)  else random.randint(0, 1)  for i1, i2 in zip(i[0][0], i[1][0]) ] for i in r]
    vec = [[ random.randint(0, 1) for i in range(0, len(items))] for i in range(0, generation_size)] + r
    return vec


for i in range(0, N):
    vec = iteration(vec, items, best, gen_size, s, size)

best = list(best)
print(items)
print('best: ')
def print_best(list_best):
    best_item = list_best[np.argmax([ i[1][0] for i in list_best])]
    print(best_item[0])
    print('weight %i' % best_item[1][1])
    print('value %i' % best_item[1][0])
print_best(best)


comb = list(itertools.product([1,0], repeat=len(items)))
print('Number of individual by brootforce = %i' % len(comb))
data = count_weight_and_value(comb, items)
data = list(filter(lambda x : x[1][1] <= size , data))
print_best(data)

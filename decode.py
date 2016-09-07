from bitarray import bitarray
import numpy as np
import itertools


def create_combinations(arr):
   return  itertools.combinations(arr, 2)


def get_seq():
    with open('encode_seq.txt') as f:
       return  f.readlines()




def get_words():
    seq = get_seq()
    print seq
    seq = seq[0]
    arr = [bitarray(x) for x in  seq.split()]
    one = arr[:5]
    two = arr[5:10]
    three = arr[10:15]
    words = [one, two, three]
    for i in words:
        i.reverse()
    return words

Sum = []
for i in  create_combinations(get_words()):   
    a = i[0] 
    b = i[1]
    Sum.append( [ t1 ^ t2 for t1, t2 in zip(a,b)])

print(Sum)




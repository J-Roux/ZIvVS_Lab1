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
  #  p))rint seq
    seq = seq[0]
    arr = [bitarray(x) for x in  seq.split()]
    arr.reverse()
    one = arr[:5]
    two = arr[5:10]
    three = arr[10:15]
    words = [one, two, three]
   # for i in words:
   #     i.reverse()
    return words

Sum = []
for i in  create_combinations(get_words()):   
    a = i[0] 
    b = i[1]
    Sum.append( [ t1 ^ t2 for t1, t2 in zip(a,b)])




def get_library():
    with open('library.txt') as f:
        return ''.join(f.readlines()).split()

def get_letters():
    with open('alphabet.txt') as f:
        return f.readlines()[0].split()

def get_bit_combinations():
    return [ bitarray(it)  for it in itertools.combinations('01', 3)]

arr = '0101'
library =[ i.replace(',', '') for i in get_library()];
comb = [bitarray(''.join(i)) for i in set([it for it in itertools.combinations_with_replacement(arr,3)])]
comb = [ i for i in itertools.permutations(comb, 8)]
letters = [ i.decode("utf-8")  for i in get_letters()];
for item in comb:
    s = { l : i   for i,l  in zip(item,letters)}
    code_library = [ [ s[i] for i in word.decode("utf-8") ] for word in library]
    check = 0
    for code in code_library:
        check = 0
        print len(Sum)
        code1 = [i ^ j for i,j in zip(code, Sum[2])]
        if code1 in code_library:
            check += 1
        else:
            break
        code2 = [i ^ j for i,j in zip(code, Sum[2])]
        if code2 in code_library:
            check += 1
        else:
            break
    if check == 2:
        for k in s:
            print k
            for v in s[k]:
                print v
        break


#word = [ s[i]  for i in word]
       # print word;
       # readkey();



from bitarray import bitarray
import numpy as np
import itertools
def create_combinations(arr):
   return  itertools.combinations(arr, 2)


def get_seq():
    with open('encode_seq.txt', encoding='utf-8') as f:
       return  f.readlines()




def get_words():
    seq = get_seq()
    seq = seq[0]
    arr = [bitarray(x) for x in  seq.split()]
    arr.reverse()
    one = arr[:5]
    two = arr[5:10]
    three = arr[10:15]
    #one.reverse()
    #two.reverse()
    #three.reverse()
    words = [one, two, three]
    return words

Sum = []
for i in  create_combinations(get_words()):   
    a = i[0] 
    b = i[1]
    Sum.append( [ t1 ^ t2 for t1, t2 in zip(a,b)])
#print (Sum)



def get_library():
    with open('library.txt',encoding='utf-8-sig') as f:
        return ''.join(f.readlines()).split()

def get_letters():
    with open('alphabet.txt', encoding='utf-8-sig') as f:
        return f.readlines()[0].split()

def get_bit_combinations():
    return [ bitarray(it)  for it in itertools.combinations('01', 3)]

arr = '0101'
library =[ i.replace(',', '') for i in get_library()];
comb = [bitarray(''.join(i)) for i in set([it for it in itertools.combinations_with_replacement(arr,3)])]
comb = [ i for i in itertools.permutations(comb, 8)]
letters = [ i  for i in get_letters()]
check = 0
result = {}
decode_words = []
for item in comb:
    s = { l : i   for i,l  in zip(item,letters)}
    code_library = [ [ s[i] for i in word] for word in library]
    if check == 2:
        break
    check = 0

    for code in code_library:
        check = 0
        code1 = [i ^ j for i,j in zip(code, Sum[1])]
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
            print(s)
            print(code)
            print(code1)
            print(code2)
            decode_dic = {s[i].to01() : i for i in s}
            print(''.join([decode_dic[i.to01()] for i in code]))
            print(''.join([decode_dic[i.to01()] for i in code1]))
            print(''.join([decode_dic[i.to01()] for i in code2]))
            result = s;
            #break

#decode_dic  = { s[i].to01(): i   for i in s}
#words = get_words()
#words = [ [ decode_dic[j.to01()] for j in i] for i in get_words()]
#print(words)
#print(decode_dic)

#word = [ s[i]  for i in word]
       # print word;
       # readkey();



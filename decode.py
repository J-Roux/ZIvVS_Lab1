from bitarray import bitarray
from numba import jit
import numpy as np
import itertools
import time


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
    words = [one, two, three]
    return words

def get_library():
    with open('library.txt',encoding='utf-8-sig') as f:
        return [ i.replace(',', '') for i in ''.join(f.readlines()).split()]

def get_letters():
    with open('alphabet.txt', encoding='utf-8-sig') as f:
        return f.readlines()[0].split()

def get_bit_combinations():
    return [ bitarray(it)  for it in itertools.combinations('01', 3)]

def get_sum():
    xor_sum = []
    for i in  create_combinations(get_words()):   
        a = i[0] 
        b = i[1]
        xor_sum.append( [ t1 ^ t2 for t1, t2 in zip(a,b)])
    return xor_sum


def get_combinations():
    arr = '0101'
    comb = [bitarray(''.join(i)) for i in set([it for it in itertools.combinations_with_replacement(arr,3)])]
    comb = [ i for i in itertools.permutations(comb, 8)]
    return comb


def get_dictionary(letters, binary_combination):
    return  { l : i   for i,l  in zip(binary_combination, letters)}


def encode_library(dictionary, library):
    return  [ [ dictionary[i] for i in word] for word in library]
@jit 
def get_code (encode_word_one, xor_sum):
    return  [i ^ j for i,j in zip(encode_word_one, xor_sum)]


def check_encode_word(encode_word_one, xor_sum, encoding_library):
    code = get_code(encode_word_one, xor_sum)
    if code in encoding_library:
        return (True, code)
    else:
        return (False, None)

def bruteforce(letters, library, xor_sum):
    binary_combinations = get_combinations()
    check = 0
    results = []
    for binary_combination in binary_combinations:
        dictionary = get_dictionary(letters, binary_combination)
        encoding_library = encode_library(dictionary, library)
        for encode_word_one in encoding_library:
            (in_library, encode_word_two) = check_encode_word(encode_word_one, xor_sum[1], encoding_library)
            if not in_library:
                break
            (in_library, encode_word_three) = check_encode_word(encode_word_one, xor_sum[2], encoding_library)
            code2 = [i ^ j for i,j in zip(encode_word_one, xor_sum[2])]
            if not in_library:
                break
            else:
                decode_dic = {dictionary[i].to01() : i for i in dictionary}
                results.append([ decode_dic,
                                 ''.join([decode_dic[i.to01()] for i in encode_word_one]),
                                 ''.join([decode_dic[i.to01()] for i in encode_word_two]),
                                 ''.join([decode_dic[i.to01()] for i in encode_word_three])
                                ])
    return results

def main():
    xor_sum = get_sum()
    library = get_library()  
    letters = get_letters()
    results = np.array(bruteforce(letters, library, xor_sum ))
    print(results)



if __name__ == '__main__':
    start = time.time()
    main()
    end = time.time()
    print(end - start) 
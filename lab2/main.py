from sympy.ntheory.factor_ import totient
from random import randint
import numpy as np
import string
from itertools import combinations

alphabet = range(ord(' '), ord('~'))
print('alphabet = %s' % ''.join([chr(i) for i in alphabet]))
a = 5 
b = 7
p = 263

print ('p = %i' % p)
print ('a = %i' % a)
print ('b = %i' % b)



def get_multiplier(val, div, mod):
    return  [ i  for i in range(0, p) if (val * i) % div == mod] 

def phi(n):
    return totient(n)

def get_param(val):
    alpha_list = get_multiplier(val, phi(p), 1)
    return alpha_list[randint(0, len(alpha_list) - 1)]


def code_text(text, a, b, p):
    alpha = get_param(a)
    beta = get_param(b)
    print('alpha = %i' % alpha)
    print('beta = %i' % beta)
    return  [ (char**a % p) ** b % p  for char in text]



        
def decode_text(encode_text, p, alphabet):
    a_t = range(0, p)
    alpha_t = [get_multiplier(i, phi(p), 1) for i in a_t]
    temp = list(
        map(
            lambda y : (y[0], y[1][0]), filter(lambda x: x[1] , zip(a_t, alpha_t))
            )
            )
    a_t = [ i[0] for i in temp]
    alpha_t = [ i[1] for i in temp]
    temp = dict(zip(alpha_t, a_t))
    u3_t = [ [char ** i % p for char in encode_text] for i in alpha_t]
    u4_t = [ [ [char ** b % p  for char in u3] for b in alpha_t] for u3 in u3_t]
    u4_t = [[ (char ** alpha[0] % p) ** alpha[1] % p  for char in encode_text] for alpha in combinations(alpha_t, 2)]
    return (list(filter(lambda x :  set(alphabet).issuperset(set(x[0])) , zip(u4_t, combinations(alpha_t, 2)))), temp)

content = ''
with open('message1.txt') as f:
    content = f.read().replace('\n', '')

print('Input = %s' % content)
content = map(lambda x : ord(x) ,list(content))



encode_text = code_text(content, a, b, p)
variants, a_map = decode_text(encode_text, p, alphabet)
result = list(map(lambda x: ([ chr(i) for i in x[0]], x[1]), variants))
keys = list(map(lambda x : x[1] ,result))
print('Number of keys = %i' % len(keys) )
text = result[0][0]
print('Output = %s' % ''.join(list(text)))





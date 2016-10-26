from sympy.ntheory.factor_ import totient
from random import randint
import numpy as np
import string
from itertools import combinations

alphabet = range(ord(' '), ord('~'))
print(''.join([chr(i) for i in alphabet]))
a = 5 
b = 7
p = 263
message = 17

print ('p = %i' % p)
print ('a = %i' % a)
print ('b = %i' % b)
print ('alpha %i' %  9)
print ('beta %i' %  19)
print ('u1 = %i' % (message ** a % p))
print ('u2 = %i' % ((message ** a % p) ** b % p))
print ('u3 = %i' % (((message ** a % p) ** b % p)  ** 9 % p))
print ('u4 = %i' % (((((message ** a % p) ** b % p) ** 19 % p) ** 9 % p) ** a % p))
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
    u3_t = [ [char ** i % p for char in encode_text] for i in alpha_t]
    u4_t = [ [ [char ** b % p  for char in u3] for b in alpha_t] for u3 in u3_t]
    u4_t = [[ (char ** alpha[0] % p) ** alpha[1] % p  for char in encode_text] for alpha in combinations(alpha_t, 2)]
    return list(filter(lambda x :  set(alphabet).issuperset(set(x[0])) , zip(u4_t, combinations(alpha_t, 2))))

content = ''
with open('message1.txt') as f:
    content = f.read().replace('\n', '')

print(content)
content = map(lambda x : ord(x) ,list(content))


#alphabet = [ 1, 17, 9, 22, 33, 533, 444]
#mes = [17,9, 9, 1,1, 1, 9, 9, 22]


encode_text = code_text(content, a, b, p)
variants = decode_text(encode_text, p, alphabet)
result = list(map(lambda x: (''.join(list([ chr(i) for i in x[0]])), x[1]), variants))
print(result)
print(np.array(list( 
    map(lambda x: ''.join(x[0]), result)
    )))

#text = list(filter(lambda x : len(x) == len(mes)  ,filter(lambda x : x ,
#        map(lambda x: filter(lambda y : y in alphabet, x)  ,variants))))
#print( len(text))
#if text:
#	print(''.join( chr(ascii_code) for ascii_code in text[0]))



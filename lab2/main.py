from sympy.ntheory.factor_ import totient
from random import randint
import numpy as np
import string

alphabet = range(ord(' '), ord('~'))
print([chr(i) for i in alphabet])
a = 5 
b = 7
p = 223


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
    return  [ (char**a % p) ** b % p  for char in text]



        
def decode_text(encode_text, p):
    alpha_t = [ encode_text[0] ** i % p for i in range(0, p)]    
    a_t = map(lambda x : x[0], filter( lambda x : x, [get_multiplier(alpha, phi(p), 1) for alpha in alpha_t]))
    beta_t = [ encode_text[0] ** a % p for a in a_t]
    b_t = map(lambda x : x[0], filter( lambda x : x, [get_multiplier(beta, phi(p), 1) for beta in beta_t]))
    u3_t = [ [ char**a % p for char in encode_text] for a in a_t]
    return np.reshape(map(lambda x :[ [ char ** b % p for char in x] for b in b_t ], u3_t),
                                    (len(a_t) * len(b_t) ,len(encode_text)))
content = ''
with open('message1.txt') as f:
    content = f.read().replace('\n', '')

print(content)
content = map(lambda x : ord(x) ,list(content))


#alphabet = [ 1, 17, 9, 22, 33, 533, 444]
mes = content #[17,9, 9, 1,1, 1, 9, 9, 22, 17]

encode_text = code_text(mes, a, b, p)
variants  = decode_text(encode_text, p)
print(len( variants))
text = filter(lambda x : len(x) == len(mes)  ,filter(lambda x : x ,
        map(lambda x: filter(lambda y : y in alphabet, x)  ,variants)))
print( len(text))
print(''.join( chr(ascii_code) for ascii_code in text[0]))



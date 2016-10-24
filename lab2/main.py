from sympy.ntheory.factor_ import totient
from random import randint
a = 5 
b = 7
p = 23 
message = 17

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
    print(alpha_t)    
    a_t = [get_multiplier(alpha, phi(p), 1) for alpha in alpha_t]
    a_t = []
    for alpha in alpha_t:
        a = get_multiplier(alpha, phi(p), 1)
        if a :
            
    #beta_t = [ encode_text[0] ** a % p for a in a_t]
    #b_t = [get_multiplier(beta, phi(p), 1) for beta in beta_t]
    print(alpha_t)
    print(a_t)
   # print(beta_t)
   # print(b_t)


encode_text = code_text([message], a, b, p)
print(encode_text)
decode_text(encode_text, p)


alpha = get_param(a)
beta = get_param(b)
print ('alpha = %i' % alpha)
print ('beta = %i' % beta)
print ('----------------------------------------------------')



print('message = %d' % message)
u1 = message ** a % p
u2 = u1 ** b % p
u3 = u2 ** alpha % p
u4 = u3 ** beta % p
print('u2 = %i' % u2)
print('u3 = %i' % u3)
print('u4 = %i' % u4)




alpha_t = [i for i in range(0, p) if u2 ** i % p == u3][0] 
print('alpha = %i' %  alpha_t)
a_t = get_multiplier(alpha_t, phi(p),1)[0]
print('a = %i' % a_t)
beta_t = u2 ** a_t % p 
print('beta = %i' % beta_t)
b_t = get_multiplier(beta_t, phi(p),1)[0]
print('b = %i' % b_t)




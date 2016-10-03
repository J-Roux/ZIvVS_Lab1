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
beta_t = u2 ** a % p 
print('beta = %i' % beta_t)
b_t = get_multiplier(beta_t, phi(p),1)[0]
print('b = %i' % b_t)




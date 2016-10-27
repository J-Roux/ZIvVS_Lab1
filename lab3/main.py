import operator
from itertools import product
from bitarray import bitarray
import os
import json

text = ''

with open('hamlet.txt') as f:
    text = list(f.read())

data_set = dict(zip(set(text), [0]*len(set(text))) )
for char in text:
    data_set[char]+=1
data_set = sorted(data_set.items(), key=operator.itemgetter(1), reverse=True)
print('-' * 30)
print('text = %s' % ''.join(text[0:100]))
print('-' * 30)

delemeter = '11'


comb = []
i = 1
while(len(comb) < len(data_set)):
    comb += filter(lambda y: (delemeter not in y) and (y[-1] != '1' ),map(lambda x: ''.join(x), product('01', repeat=i)))
    i+=1
comb = comb[:len(data_set)]
coding_map = { i[0]:bitarray(j)  for i,j in zip(data_set, comb)}
coding_map_ser = { i[0]:j  for i,j in zip(data_set, comb)}
decode_dict = coding_map_ser
coding_map['^'] = bitarray(delemeter)
coding_map_ser['^'] = delemeter
delemeter_list = ['^'] * len(text)

result = [None] * (len(text) * 2)

result[::2] = text
result[1::2] = delemeter_list
encoding_text = bitarray()
encoding_text.encode(coding_map, result)
print('original size = %i' % os.stat('hamlet.txt').st_size)
with open('result.txt', 'w+') as f:
    f.write(json.dumps(coding_map_ser))
with open('result.txt', 'ab+') as f:
    f.write(encoding_text.tobytes())
print('compressed size = %i' % os.stat('result.txt').st_size)
print('coeff = %f' % ( os.stat('hamlet.txt').st_size / os.stat('result.txt').st_size))

with open('result.txt', 'rb') as f:
    text = f.read()

decode_dict = { v : k for k,v in decode_dict.items()}
JSON = text[:text.index(ord('}'))+1]
d = json.loads(JSON.decode('ascii'))
data = text[text.index(ord('}'))+1:]
l = bitarray()
l.frombytes(data)
val = l.to01().split(delemeter)
val = val[:len(val) - 1]
print('-' * 30)
print('result  = %s' % ''.join(map(lambda x : decode_dict[x], val))[:100])
print('-' * 30)

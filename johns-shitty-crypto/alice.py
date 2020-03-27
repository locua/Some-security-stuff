import bitarray
import random, string

def randomword(length):
   letters = string.printable
   return ''.join(random.choice(letters) for i in range(length))

message = "hello my old friend"
m = bitarray.bitarray()
ka = bitarray.bitarray()
kb = bitarray.bitarray()
m.frombytes(message.encode('utf-8'))
keya = randomword(len(message))
keyb = randomword(len(message))
ka.frombytes(keya.encode('utf-8'))
kb.frombytes(keyb.encode('utf-8'))
c = ka ^ m
d = c ^ kb
e = d ^ ka
out = e ^ kb
#print(m)
#print(ka)
#print(kb)
print(c)
print(d)
print(e)
# it works?
print("out: %s " % out.tobytes())
# Charlie, who can only see c, d and e, can decrypt the original message without the keys
print("charlie:")
print((c^d^e).tobytes())


'''
example
m = 0110

ka = 1010
kb = 0100

m XOR ka = c = 1100
m XOR ka XOR kb = d = 1000
m XOR ka XOR kb XOR ka = e = 0110
m XOR ka XOR kb XOR ka XOR kb = m = 0110
'''


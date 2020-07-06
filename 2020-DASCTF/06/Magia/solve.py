#!/usr/bin/env python
from z3 import *

v13 = [0x33, 0, 0x15, 9, 0xB, 0x36, 6, 0xC, 2, 0x3A, 0x2C, 8, 0x31, 0xB, 0x37, 0xC]
v12 = [0x4C, 0x65, 0x60, 0x72, 0x64, 0x49, 0x70, 0x63, 0x6C, 0x45, 0x53, 0x61, 0x4E, 0x64, 0x48, 0x61]
v11 = [0xE, 5, 0, 0xB, 0xD, 9, 2, 3, 0xC, 5, 0xF, 1, 0xE, 4, 0xF, 0xD, 1, 8, 0xF, 0xF, 9, 3, 0xF, 0xE, 0xF, 4, 0xF, 6, 2, 5, 5, 0xD]

flag = [BitVec('x%d' % i, 8) for i in range(32)]
s = Solver()

s.add(flag[0] == ord('N'))
s.add(flag[1] == ord('e'))
s.add(flag[2] == ord('p'))
s.add(flag[3] == ord('{'))
s.add(flag[31] == ord('}'))

for j in range(16):
    i = 31 - j
    s.add(flag[i] ^ flag[j] == v13[j])
    s.add(flag[i] & flag[j] == v12[j])
    s.add(flag[j] & 0xF == v11[j])
    s.add(flag[i] & 0xF == v11[i])

s.add(flag[10] == ord('_'))
s.add(flag[14] == ord('_'))
s.add(flag[19] == ord('_'))
s.add(flag[22] == ord('_'))
s.add(flag[26] == ord('_'))

if s.check() == sat:
    #print s.model()
    flag = ''.join([chr(eval(str(s.model()[c]))) for c in flag])
    print flag

ans = ''
v2 = [0x25, 0x6E, 0x31, 0x13, 0x2F, 0x28, 0x20, 0x3C, 0x35, 0x34, 0x30, 0x6D, 0x3B, 0x36, 7, 0x3C, 0x38, 0x7F, 0x5D, 0x54, 0x28, 0x1E, 0x1A, 0x2F, 0x3B, 0x2B, 0x55, 0x36, 0x49, 0x6D, 0x66, 0x7E]
v5 = 'Sis_puella_magica!'
for i in range(32):
    ans += chr(ord(v5[i % 18]) ^ v2[i] ^ ord(flag[i]))
print ans

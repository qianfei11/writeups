#!/usr/bin/env python
enc = [0xB3, 0x9C, 0xB7, 0xBF, 0xB2, 0xCB, 0xD3, 0xBF, 0xB2, 0xCB, 0xD3, 0xC9, 0xB1, 0xCB, 0xD3, 0xBB, 0xAE, 0xAD, 0xA3, 0xCF, 0xAD, 0xCD, 0x9F, 0xBB]

v11 = [0xE3, 0xE5, 0xF3, 0xF3, 0xF5, 0xE3, 0xE3, 0x90]
for i in range(len(v11)):
    v11[i] ^= 0x90
v5 = [0xF6, 0xF1, 0xF9, 0xFC, 0xF4, 0x90]
for i in range(len(v5)):
    v5[i] ^= 0x90
print ''.join([chr(c) for c in v11])
print ''.join([chr(c) for c in v5])

def encrypt(s):
    res = ''
    k = 0
    v5 = 0
    idx = 0
    while True:
        if idx >= len(s):
            break
        res += chr((v5 | (ord(s[idx]) >> (k + 2)) - 106) & 0xFF)
        k = (k + 2) & 7
        for i in range(k):
            v5 |= ((ord(s[idx]) & (1 << i)) << (6 - k))
        if k <= 5:
            idx += 1
    return res

print encrypt('123')


#!/usr/bin/env python
from z3 import *

bf = '****--:~+******^.~+*****:*+++++^.-:///--*^.:///---^.,:~-----^>,:~-/++++++++++++^>,:~+****--^>+*******://++++++++++^:,^>-:///^:,^>+******://-^:,^>-/+://+++++++^:,^>-/----:,^>-/+:/+++++^:,^>-:++****+^:,^>-/+:~+**++^:,^>+****:*^:,^>-:++****++++^:,^>-/---:,^>+*****://+^:,^>-/+:///+^:,^>,'

choices = [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x06, 0x0B, 0x07, 0x0B, 0x08, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x09, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0B, 0x0A]

data = [0xFA, 0x2B, 0x94, 0xEA, 0x63, 0xA8, 0xC4, 0x13, 0x84, 0xE7, 0xA7, 0xDA, 0xD4, 0x2D, 0xAE, 0xBE, 0x7D, 0x00, 0x00, 0x00, 0x98, 0xD7, 0x41]

flag = [BitVec('x%d' % i, 8 + 1) for i in range(17)]

arr = [0 for i in range(17)]
arr[0] = 1
ax = 0
bx = 0
idx = 0
for c in bf:
    x = choices[ord(c) - 0x2A]
    if x == 0:
        arr[ax] *= 2
    if x == 1:
        arr[ax] += 1
    if x == 2:
        arr[ax] = flag[idx]
        idx += 1
    if x == 3:
        arr[ax] -= 1
    if x == 4:
        continue
    if x == 5:
        arr[ax] >>= 1
    if x == 6:
        bx = arr[ax]
    if x == 7:
        ax -= 1
    if x == 8:
        ax += 1
    if x == 9:
        arr[ax] ^= bx
    if x == 10:
        if ax == 0x20:
            break
        arr[ax] = 0
    arr[ax] &= 0xff
    ax &= 0xff
    bx &= 0xff

s = Solver()
for i in range(16):
    s.add(data[i] == arr[i])
if s.check() == sat:
    print s.model()
    flag.pop()
    flag = ''.join([hex(int(str(s.model()[flag[i]])))[2:].zfill(2) for i in range(16)])
    print flag


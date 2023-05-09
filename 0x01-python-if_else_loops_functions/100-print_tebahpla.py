#!/usr/bin/python3
m = 0
for le in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(le - m)), end="")
    m = 32 if m == 0 else 0

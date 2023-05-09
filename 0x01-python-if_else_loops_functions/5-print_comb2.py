#!/usr/bin/python3
for m in range(0, 100):
    if m == 99:
        print(m)
    else:
        print("{:02}".format(m), end=", ")

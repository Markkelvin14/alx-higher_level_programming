#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    no = 0
    dn = 0
    for toople in my_list:
        no += toople[0] * toople[1]
        dn += toople[1]
        return (no / dn)

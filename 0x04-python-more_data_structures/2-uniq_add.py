#!/usr/bin/python3
def uniq_add(my_list=[]):
    lists = set(my_list)
    no = 0

    for m in lists:
        no += m

    return (no)

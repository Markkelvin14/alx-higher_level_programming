#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dic = a_dictionary.copy()
    lists = list(new_dic.keys())
    for m in lists:
        new_dic[m] *= 2
    return (new_dic)

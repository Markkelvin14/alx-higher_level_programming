#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    lists = list(a_dictionary)
    lists.sort()
    for m in lists:
        print("{}: {}".format(m, a_dictionary.get(m)))

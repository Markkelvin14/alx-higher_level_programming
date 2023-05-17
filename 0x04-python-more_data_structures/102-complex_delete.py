#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    lists = list(a_dictionary.keys())
    for value_spec in lists:
        if value == a_dictionary.get(value_spec):
            del a_dictionary[value_spec]
    return (a_dictionary)

#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    ans = 0
    for m in range(0, x):
        try:
            print("{:d}".format(my_list[m]), end="")
            ans += 1
        except (TypeError, ValueError):
            continue
    print("")
    return (ans)

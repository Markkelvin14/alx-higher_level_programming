#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    for m in range(0, list_length):
        try:
            ans = my_list_1[m] / my_list_2[m]
        except TypeError:
            print("wrong type")
            ans = 0
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        finally:
            newlist.append(ans)
    return (newlist)

#!/usr/bin/python3
def safe_print_division(a, b):
    ans = 0
    try:
        ans = int(a) / int(b)
    except (TypeError, ZeroDivisionError):
        ans = None
    finally:
        print("Inside result: {}".format(ans))
    return (ans)

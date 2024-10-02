#!/usr/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            if i < len(my_list):
                if count > 0:
                    print("", end='')
                print(my_list[i], end='')
                count += 1
    except IndexError:
        pass
    print()
    return count

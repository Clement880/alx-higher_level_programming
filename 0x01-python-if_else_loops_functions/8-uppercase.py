#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ite in str:
        if 'a' <= ite <= "z":
            result += chr(ord(ite) - 32)
        else:
            result += ite
    print("{}".format(result))

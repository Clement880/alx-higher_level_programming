#!/usr/bin/python3
def uppercase(str):
    result = ""
    for ite in str:
        if ord(ite) >= 97 and ord(ite) <= 122:
            result += chr(ord(ite) -32)
        else:
            result += ite
    print(result)

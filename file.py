from ctypes import *

adder = CDLL('/adder.so')

a, b = int(input()), int(input())

res_int = adder.add_int(a,b)

print(res_int)


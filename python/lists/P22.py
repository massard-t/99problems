# encoding: utf-8

# 1.22 (*) Create a list containing all integers within a given range.
#     Example:
#     ?- range(4,9,L).
#     L = [4,5,6,7,8,9]


def func(min, max):
    return range(min, max+1)
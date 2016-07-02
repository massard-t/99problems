# encoding: utf-8

# 1.03 (*) Find the K'th element of a list.
#     The first element in the list is number 1.
#     Example:
#     ?- element_at(X,[a,b,c,d,e],3).
#     X = c


def func(data, pos):
    return data[pos-1]
# encoding: utf-8

# 1.21 (*) Insert an element at a given position into a list.
#     Example:
#     ?- insert_at(alfa,[a,b,c,d],2,L).
#     L = [a,alfa,b,c,d]


def func(to_insert, data, pos):
    return data[:pos-1] + [to_insert] + data[pos-1:]
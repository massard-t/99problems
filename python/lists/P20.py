# encoding: utf-8

# 1.20 (*) Remove the K'th element from a list.
#     Example:
#     ?- remove_at(X,[a,b,c,d],2,R).
#     X = b
#     R = [a,c,d]


def func(data, x):
    data.pop(x-1)
    return data
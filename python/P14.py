# encoding: utf-8

# 1.14 (*) Duplicate the elements of a list.
#     Example:
#     ?- dupli([a,b,c,c,d],X).
#     X = [a,a,b,b,c,c,c,c,d,d]


def func(data):
    res = []
    for element in data:
        res.append(element)
        res.append(element)
    return res

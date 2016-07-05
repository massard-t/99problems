# encoding: utf-8

# 1.08 (**) Eliminate consecutive duplicates of list elements.
#     If a list contains repeated elements they should be replaced with a single copy of the element. The order of the elements should not be changed.
#
#     Example:
#     ?- compress([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
#     X = [a,b,c,a,d,e]


def func(data):
    res = data[:1]
    for elem in data[1:]:
        if elem != res[-1]:
            res.append(elem)
    return res
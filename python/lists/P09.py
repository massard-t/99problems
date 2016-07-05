# encoding: utf-8

# 1.09 (**) Pack consecutive duplicates of list elements into sublists.
#     If a list contains repeated elements they should be placed in separate sublists.
#
#     Example:
#     ?- pack([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
#     X = [[a,a,a,a],[b],[c,c],[a,a],[d],[e,e,e,e]]


def func(data):
    last_elem = data[:1][0]
    res = []
    counter = 1
    for elem in data[1:]:
        if elem == last_elem:
            counter += 1
        if elem != last_elem:
            res.append([last_elem] * counter)
            counter = 1
        last_elem = elem
    res.append([last_elem] * counter)
    return res
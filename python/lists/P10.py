# encoding: utf-8

# 1.10 (*) Run-length encoding of a list.
#     Use the result of problem 1.09 to implement the so-called run-length encoding data compression method. Consecutive duplicates of elements are encoded as terms [N,E] where N is the number of duplicates of the element E.
#
#     Example:
#     ?- encode([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
#     X = [[4,a],[1,b],[2,c],[2,a],[1,d][4,e]]


def func(data):
    last_elem = data[:1][0]
    res = []
    counter = 1
    for elem in data[1:]:
        if elem == last_elem:
            counter += 1
        if elem != last_elem:
            res.append([counter, last_elem])
            counter = 1
        last_elem = elem
    res.append([counter, last_elem])
    return res
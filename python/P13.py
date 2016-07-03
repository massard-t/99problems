# encoding: utf-8

# 1.13 (**) Run-length encoding of a list (direct solution).
#     Implement the so-called run-length encoding data compression method directly. I.e. don't explicitly create the sublists containing the duplicates, as in problem 1.09, but only count them. As in problem 1.11, simplify the result list by replacing the singleton terms [1,X] by X.
#
#     Example:
#     ?- encode_direct([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
#     X = [[4,a],b,[2,c],[2,a],d,[4,e]]


def func(data):
    def how_to_append(count, last):
        if count == 1:
            return last
        else:
            return [count, last]
    last_elem = data[:1][0]
    res = []
    counter = 1
    for elem in data[1:]:
        if elem == last_elem:
            counter += 1
        if elem != last_elem:
            res.append(how_to_append(counter, last_elem))
            counter = 1
        last_elem = elem
    res.append(how_to_append(counter, last_elem))
    return res
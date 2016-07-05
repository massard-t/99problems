# encoding: utf-8

# 1.11 (*) Modified run-length encoding.
#     Modify the result of problem 1.10 in such a way that if an element has no duplicates it is simply copied into the result list. Only elements with duplicates are transferred as [N,E] terms.
#
#     Example:
#     ?- encode_modified([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
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
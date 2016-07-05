# encoding: utf-8

# 1.07 (**) Flatten a nested list structure.
#     Transform a list, possibly holding lists as elements into a 'flat' list by replacing each list with its elements (recursively).
#
#     Example:
#     ?- my_flatten([a, [b, [c, d], e]], X).
#     X = [a, b, c, d, e]
#
#     Hint: Use the predefined predicates is_list/1 and append/3


def funcl(data):
    if data == []:
        return data
    if isinstance(data[0], list):
        return funcl(data[0]) + funcl(data[1:])
    return data[:1] + funcl(data[1:])
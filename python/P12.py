# encoding: utf-8

# 1.12 (**) Decode a run-length encoded list.
#     Given a run-length code list generated as specified in problem 1.11. Construct its uncompressed version.


def func(data):
    result = []
    for element in data:
        if isinstance(element, list):
            for _ in xrange(element[0]):
                result.append(element[1])
        else:
            result.append(element)
    return result
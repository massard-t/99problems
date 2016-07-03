# encoding: utf-8

# 1.15 (**) Duplicate the elements of a list a given number of times.
#     Example:
#     ?- dupli([a,b,c],3,X).
#     X = [a,a,a,b,b,b,c,c,c]
#
#     What are the results of the goal:
#     ?- dupli(X,3,Y).


def func(data, times):
    res = []
    for ele in data:
        res = sum([[ele] * times], res)
    return res
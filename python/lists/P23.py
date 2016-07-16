# encoding: utf-8

# 1.23 (**) Extract a given number of randomly selected elements from a list.
#     The selected items shall be put into a result list.
#     Example:
#     ?- rnd_select([a,b,c,d,e,f,g,h],3,L).
#     L = [e,d,a]
import random


def func(data, to_pop):
    res = []
    for _ in xrange(to_pop):
        res.append(data.pop(random.randrange(0, len(data)-1)))
    return res

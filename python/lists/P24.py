# encoding: utf-8

# 1.24 (*) Lotto: Draw N different random numbers from the set 1..M.
#     The selected numbers shall be put into a result list.
#     Example:
#     ?- rnd_select(6,49,L).
#     L = [23,1,17,33,21,37]
import random


def func(total, max):
    res = []
    for _ in xrange(total):
        res.append(random.randrange(0, max))
    return res

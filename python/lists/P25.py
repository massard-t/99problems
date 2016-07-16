# encoding: utf-8

# 1.25 (*) Generate a random permutation of the elements of a list.
#     Example:
#     ?- rnd_permu([a,b,c,d,e,f],L).
#     L = [b,a,d,c,e,f]
import random


def func(data):
    value_one = random.randrange(0, len(data)-1)
    value_two = random.randrange(0, len(data)-1)
    data[value_one], data[value_two] = data[value_two], data[value_one]
    return data
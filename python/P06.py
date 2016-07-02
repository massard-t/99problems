# encoding: utf-8

# 1.06 (*) Find out whether a list is a palindrome.
#     A palindrome can be read forward or backward; e.g. [x,a,m,a,x].


def func(data):
    return data == data[::-1]

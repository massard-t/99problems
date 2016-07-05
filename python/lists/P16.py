# encoding: utf-8

# 1.16 (**) Drop every N'th element from a list.
#     Example:
#     ?- drop([a,b,c,d,e,f,g,h,i,k],3,X).
#     X = [a,b,d,e,g,h,k]


def func(data, pos):
    del data[pos-1]
    return data

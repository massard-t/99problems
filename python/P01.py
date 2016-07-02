# encoding: utf-8

# 1.01 (*) Find the last element of a list.
#     Example:
#     ?- my_last(X,[a,b,c,d]).
#     X = d

def p01(data):
    return data[-1]

if __name__ == '__main__':
    print(p01([1, 2, 3, 4, 5]))